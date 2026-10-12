import argparse
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress


def load_data(filename):

    """Load polarization data and standardize its column names."""

    data = pd.read_csv(filename)

    # Accept either of the column-name formats used in our project.

    column_mapping = {

        "Potential (V)": "potential_V",

        "Current Density (A/cm^2)": "current_density_A_cm2",

    }

    data = data.rename(columns=column_mapping)

    # Check that the required columns are available.

    required_columns = {"potential_V", "current_density_A_cm2"}

    if not required_columns.issubset(data.columns):

        raise ValueError(

            "CSV must contain potential and current-density columns. "

            f"Columns found: {data.columns.tolist()}"

        )

    # Convert the columns to numbers and discard invalid rows.

    for column in required_columns:

        data[column] = pd.to_numeric(data[column], errors="coerce")

    data = data.replace([np.inf, -np.inf], np.nan).dropna(

        subset=["potential_V", "current_density_A_cm2"]

    )

    # Calculate the absolute current density for logarithmic plotting.

    data["absolute_current"] = data["current_density_A_cm2"].abs()

    # Zero current cannot be used in a logarithmic Tafel fit.

    data = data[data["absolute_current"] > 0].copy()

    if len(data) < 10:

        raise ValueError(

            "Not enough nonzero current-density data points for Tafel analysis."

        )

    return data

def fit_tafel_region(data, potential_min, potential_max):

    """Fit a straight line to a selected Tafel region."""

    # Select data within the specified potential range.

    selected_data = data[

        (data["potential_V"] >= potential_min)

        & (data["potential_V"] <= potential_max)

    ].copy()

    # A linear regression needs at least three data points.

    if len(selected_data) < 3:

        raise ValueError(

            f"Not enough data points between {potential_min} V "

            f"and {potential_max} V."

        )

    # Remove zero currents because log10(0) is undefined.

    selected_data = selected_data[

        selected_data["absolute_current"] > 0

    ].copy()

    if len(selected_data) < 3:

        raise ValueError(

            "Not enough nonzero current values in the selected Tafel region."

        )

    # Convert current density to its base-10 logarithm.

    log_current = np.log10(selected_data["absolute_current"])

    # Fit log10(current density) against potential.

    fit = linregress(

        selected_data["potential_V"],

        log_current

    )

    return fit, selected_data


def calculate_tafel_parameters(data, anodic_window, cathodic_window):
    """Estimate Ecorr, icorr, and Tafel slopes from selected fitting regions."""

    # Fit the anodic and cathodic branches separately.
    anodic_fit, anodic_data = fit_tafel_region(
        data, anodic_window[0], anodic_window[1]
    )

    cathodic_fit, cathodic_data = fit_tafel_region(
        data, cathodic_window[0], cathodic_window[1]
    )

    # Find the intersection of the two fitted lines.
    # Each line has the form log10(i) = slope * E + intercept.
    denominator = anodic_fit.slope - cathodic_fit.slope

    if abs(denominator) < 1e-12:
        raise ValueError("The fitted Tafel lines are nearly parallel.")

    ecorr = (cathodic_fit.intercept - anodic_fit.intercept) / denominator

    log_icorr = anodic_fit.slope * ecorr + anodic_fit.intercept
    icorr = 10 ** log_icorr

    # Convert fitted slopes into conventional Tafel slopes in V/decade.
    beta_a = 1 / anodic_fit.slope
    beta_c = -1 / cathodic_fit.slope

    return {
        "ecorr": ecorr,
        "icorr": icorr,
        "beta_a": beta_a,
        "beta_c": beta_c,
        "anodic_fit": anodic_fit,
        "cathodic_fit": cathodic_fit,
        "anodic_data": anodic_data,
        "cathodic_data": cathodic_data,
    }


def calculate_corrosion_rate(icorr, metal):
    """Estimate corrosion rate in mm/year using current density in A/cm²."""

    # Approximate equivalent weights and densities for selected metals.
    metal_properties = {
        "Al": {"equivalent_weight": 8.99, "density": 2.70},
        "Zn": {"equivalent_weight": 32.69, "density": 7.14},
        "Fe": {"equivalent_weight": 27.92, "density": 7.87},
    }

    if metal not in metal_properties:
        raise ValueError("Choose a supported metal: Al, Zn, or Fe.")

    properties = metal_properties[metal]

    # Faraday-law conversion to penetration rate in mm/year.
    icorr_microamps = icorr * 1e6

    corrosion_rate = (
        3.27e-3
        * icorr_microamps
        * properties["equivalent_weight"]
        / properties["density"]
    )

    return corrosion_rate


def plot_results(data, results, output_filename="tafel_plot.png"):
    """Plot measured synthetic data and the fitted Tafel lines."""

    potential = data["potential_V"].to_numpy()
    current = data["current_density_A_cm2"].to_numpy()

    # Plot anodic and cathodic current magnitudes on a logarithmic scale.
    plt.figure(figsize=(10, 6))
    plt.semilogy(
        potential[current > 0],
        np.abs(current[current > 0]),
        "o",
        markersize=3,
        label="Anodic data",
    )
    plt.semilogy(
        potential[current < 0],
        np.abs(current[current < 0]),
        "o",
        markersize=3,
        label="Cathodic data",
    )

    # Extend each fitted line across its selected fitting region.
    for fit_key, data_key, label in [
        ("anodic_fit", "anodic_data", "Anodic Tafel fit"),
        ("cathodic_fit", "cathodic_data", "Cathodic Tafel fit"),
    ]:
        fit = results[fit_key]
        region = results[data_key]
        e_fit = np.linspace(
            region["potential_V"].min(),
            region["potential_V"].max(),
            100,
        )
        log_i_fit = fit.slope * e_fit + fit.intercept
        plt.semilogy(e_fit, 10 ** log_i_fit, "-", label=label)

    # Mark the estimated corrosion potential and current density.
    plt.plot(
        results["ecorr"],
        results["icorr"],
        "x",
        markersize=10,
        label="Estimated corrosion point",
    )

    plt.xlabel("Potential (V)")
    plt.ylabel("Absolute current density (A/cm²)")
    plt.title("Tafel Analysis of Polarization Data")
    plt.grid(True, which="both", alpha=0.3)
    plt.legend()
    plt.tight_layout()
    plt.savefig(output_filename, dpi=300)
    plt.show()

    print(f"Plot saved as {output_filename}")


def main():
    """Read command-line arguments, analyse the data, and print results."""

    parser = argparse.ArgumentParser(
        description="Estimate corrosion parameters from polarization data."
    )

    parser.add_argument("filename", help="Input polarization CSV file")
    parser.add_argument("--area", type=float, default=1.0,
                        help="Exposed electrode area in cm² (default: 1.0)")
    parser.add_argument("--metal", choices=["Al", "Zn", "Fe"], default="Al",
                        help="Metal used for corrosion-rate calculation")

    args = parser.parse_args()

    if args.area <= 0:
        parser.error("Electrode area must be greater than zero.")

    # Read the data and estimate the corrosion parameters.
    data = load_data(args.filename)

    # These are initial fitting windows; we will inspect the results.
    anodic_window = (-0.42, -0.30)

    cathodic_window = (-0.70, -0.58)

    results = calculate_tafel_parameters(
        data, anodic_window, cathodic_window
    )

    corrosion_rate = calculate_corrosion_rate(
        results["icorr"], args.metal
    )

    print("\n--- Tafel Analysis Results ---")
    print(f"Estimated corrosion potential: {results['ecorr']:.4f} V")
    print(f"Estimated icorr: {results['icorr'] * 1e6:.2f} µA/cm²")
    print(f"Anodic Tafel slope: {results['beta_a'] * 1000:.2f} mV/decade")
    print(f"Cathodic Tafel slope: {results['beta_c'] * 1000:.2f} mV/decade")
    print(f"Estimated corrosion rate: {corrosion_rate:.4f} mm/year")
    print(f"Metal: {args.metal}")
    print(f"Electrode area supplied: {args.area:.2f} cm²")

    # Display the plot and save a copy as a PNG image.
    plot_results(data, results)


if __name__ == "__main__":
    main()
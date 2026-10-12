import numpy as np
import pandas as pd


def generate_synthetic_data():
    """Generate synthetic electrochemical polarization data."""

    # Make the results reproducible
    np.random.seed(42)

    # Define the corrosion parameters
    icorr = 49.67e-6  # Corrosion current density, A/cm²
    ecorr = -0.50     # Corrosion potential, V
    beta_a = 0.060    # Anodic Tafel slope, V/decade
    beta_c = 0.120    # Cathodic Tafel slope, V/decade

    # Generate potential values
    potential = np.linspace(-0.80, -0.20, 301)

    # Calculate overpotential
    eta = potential - ecorr

    # Calculate anodic and cathodic partial currents
    anodic_current = icorr * 10 ** (eta / beta_a)
    cathodic_current = -icorr * 10 ** (-eta / beta_c)

    # Calculate net current density
    current_density = anodic_current + cathodic_current

    # Add small relative noise
    noise = np.random.normal(0, 0.025, len(current_density))
    current_density = current_density * (1 + noise)

    # Store the data
    data = pd.DataFrame({
        "Potential (V)": potential,
        "Current Density (A/cm^2)": current_density
    })

    # Save the CSV file
    data.to_csv("synthetic_data.csv", index=False)

    print("Synthetic polarization data generated successfully.")
    print(f"Number of data points: {len(data)}")
    print(f"Known corrosion current density: {icorr * 1e6:.2f} µA/cm²")
    print(f"Known corrosion potential: {ecorr:.3f} V")
    print(f"Known anodic Tafel slope: {beta_a * 1000:.0f} mV/decade")
    print(f"Known cathodic Tafel slope: {beta_c * 1000:.0f} mV/decade")
    print(f"Minimum current density: {data['Current Density (A/cm^2)'].min():.6e} A/cm²")
    print(f"Maximum current density: {data['Current Density (A/cm^2)'].max():.6e} A/cm²")


if __name__ == "__main__":
    generate_synthetic_data()
# Tafel-Analysis-
Python analysis of synthetic and experimental electrochemical polarization data

Tafel Analysis and Plot

Tafel Analysis

A Tafel analysis is a way to  estimate how fast a metal is corroding by measuring the electrical current produced by the electrochemical reaction on its surface.

Tafel analysis tells us:

1.How fast the metal sample is corroding.
2.If corrosion inhibitor reduces/decreases corrosion rate in the metal
3.How much protection the inhibitor provides

What happens when metal corrodes?

There’s two reaction involved when metal corrodes.

First there’s anodic reaction: this anodic reaction which is the negative electrode, occur at the anode and cause a metal to lose an electron and making the metal dissolve, and by result we have oxidation reaction.

Al → Al3+  + 3e- −−−−−−−−−(1) 

On the other hand;

There’s the cathodic reaction which occurs at the cathode, this positive electrode consumes electron transferred from the negative electrode through the electrical conductivity (wire) and if  hydrogen is available in the reaction then hydrogen ions( H+) is reduced to hydrogen gas (H2) and therefore we have a reduction reaction.

2H+ + 2e− → H2 −−−−−−− (2)

The overall reaction during this process is know as Electrochemical 
reaction.

Note: electrons do not necessary have to move through solution. They move through electrical conducting metals, while ions carries charge through electrolyte.

What is Corrosion potential (Ecorr)?

Imagine you put a metal sample (aluminium coupon) in a acidic environment and connect it to some kind of electrochemical instrument to measure the potential  of the metal with respect to a reference electrode, and the unit of measurement is in volts (V)  and millivolt (mV) for corrosion studies. 

As the metal continues to corrode, the potential (V) of the metal begins to settle around a value know as Corrosion Potential (Ecorr) during the experimental condition. 

At this potential, Both the anodic and cathode occur at equal reaction rate when expressed in terms of current magnitude.

For example:
Anodic current: +50μA
Cathodic current : −50μA


Net current density, i_net = 50-50 = 0

Which means Zero current, and this does not mean that corrosion has stopped. But it is just to tell us that the current reaction is balanced.

What is Corrosion Current Density (Icorr)?

Corrosion current density is defined as the the current per unit Area measured in A/cm2   or Acm-2 

I_corr  = IA 

Icorr = Corrosion current density

Icorr = electric current

A = Area covered

Note:

E_corr : tells us the potential at which the anodic and cathodic current is balanced

I_corr :  Tells us the magnitude of those opposing current at the potential, and it is used to estimate the corrosion rate.

What happens when the applied potential is moved away from Corrosion potential E_corr?


Two things happens when you move the applied Potential of the corrosion metal away from the Corrosion potential  Ecorr  and this is where Tafel analysis becomes useful.

Instead of allowing the metal to corrode at its natural potential, an electrochemical instrument can deliberately change the applied potential to measure the resulting potential.

This experiment is known as the Potentiodynamic polarization test

This electrochemical instrument can scan the applied potential in both the negative and positive direction relative to  the corrosion potential E_corr 

    1.If  the potential is move towards the positive side: This makes the potential to be more positive relative to corrosion potential.

    This positive movement of the potential favours the anodic reaction, making metal oxidation more significant.

    2.If the potential is moved towards the negative direction: The potential becomes more negative relative to the corrosion potential.

    This favours the cathodic reaction, making the reduction more significant.

When Potential Nears E_corr, the reaction rate between cathode and anode is equal. Therefore their current rate is balanced.

I = Ia - Ic = 0
When Applied Potential becomes more positive 	 The anode current becomes more dominant
When Applied Potential becomes more negative	The cathode current becomes more dominant





Tafel plot

Tafel plot is a graph used to examine how the measure current changes as the electrode potential changes.

It has two axes:

Horizontal axis: Logarithm of the absolute current density |i|  measured in A/cm2  
 The scale is log in the x axis.

Vertical axis: Electrode potential Ecorr 
The Horizontal axis is logarithmic because electrochemical currents can vary by several orders of magnitude.
For example, the current density might change from:
1 μ A/cm2  
to 
10 μ A/cm2  
to 
100 μ A/cm2 
On a logarithmic axis, these values are evenly spaced because each represents a tenfold increase. 
Why do straight lines appears
Under suitable condition, the anodic and cathodic current follows the Tafel relationship
For anodic branch:
E = Ecorr + βalog10(iaicorr)

For Cathodic branch:

E = Ecorr − βclog10(|ic|icorr)
Here:
E is the applied potential.
Ecorr is the corrosion potential.
icorr is the corrosion current density.
βa is the anodic Tafel slope.
βc is the magnitude of the cathodic Tafel slope.
The Tafel slopes are commonly expressed in mV per decade.
A “decade” means a tenfold change in current density.
For example:
if a Tafel slope is 120 mV/decade, the potential changes by approximately 120 mV for each tenfold increase in the relevant branch current, within the region where the Tafel relationship holds.
How do we obtain Ecorr  and Icorr
This is where Tafel exploration comes into play.
Suppose you have measured the polarization curve and identified two regions.
1.A suitable linear region for anodic branch.
2.A suitable linear region for the cathodic branch.
You fit a straight line to each region and extend the fitted lines toward the corrosion potential.
Their intersection estimates the Ecorr and Icorr.
Note: The corrosion potential is read from the vertical coordinate, and the corrosion current density is read from the logarithmic current-density coordinate.
Note: Icorr  measured from the exploration is not same as the net zero current from the Corrosion Potential.
What does extrapolation mean?
Extrapolation means extending a relationship beyond the region where you fitted it.

Mixed Anodic-Cathodic Tafel Equation

i= icorr10E −Ecorrβa   − 10E −Ecorrβc
This is a simplified form of the mixed anodic-cathodic Tafel equation.
It describes the net current density as the difference between the anodic and cathodic contributions.
i = Net current density
icorr = Corrosion current density
E = Applied potential
Ecorr = Corrosion potential
βa = anodic Tafel slope
βc  = cathodic Tafe slope

When E = Ecorr both exponents equal zero.
Since 100 = 1:
i=icorr (1-1)=0 
This agrees with our earlier explanation: the opposing reaction currents balance at the corrosion potential.

How to convert  icorr for corrosion rate
Suppose your Tafel analysis gives :
Icorr  = 50μ A/cm2
You now want to express corrosion as an estimated metal thickness lost per year.
For this conversion, your notes give the ASTM G102 relationship:
CR = 3.27 × 10-3 icorr EWρ
where:
CR = corrosion rate in mm/year.
Icorr  = corrosion current density in μ A/cm2
EW = equivalent weight in g/equivalent
ρ = density in g/cm³
Equivalent weight EW =  Mola massNo. of electronss transffred during the reaction = Mmn
For example the equivalent weight of aluminium can be calculated as:
Al → Al 3+  + 3e−  
 The electrons transferred here is 3
EW = 26.983 ≈ 8.99 
For Zn2+ 
EW = 65.382 ≈32.69 
And so on.




Work Example for Aluminium :
Suppose you were given this details
Icorr = 50 μ A/cm2 
EW = 8.99 
ρ = 2.79 g/cm3 

CR = 3.27 Χ 10-3  icorr x EWρ
Icorr  x 8.99 = 50 x 8.99 = 449.5
449.5 / 2.79 = 166.48
CR = 3.27 x 10−3 x 166.48 = 0.544 mm/year

CR = 0.544mm/year  

What does inhibition efficiency mean in your research?

You studied whether neem leaf extract could reduce the corrosion of cast A356 aluminium alloy in hydrochloric acid.

You need to compare two conditions:
1.Blank: Aluminium in the acid without neem extract.
2.Inhibited: Aluminium in the acid containing neem extract.
 IE% = Inhibition efficiency
IE% = iblank − iinhiblank x 100
i  = icorr 
Given iblank = 100 μ A/cm2 
iinh = 40 μ A/cm2 
IE% = 100 − 40100  x 100 =  60%
What does 60% mean?
It means that the inhibitor-treated specimen had a corrosion current density 60% lower than the blank specimen under those experimental conditions.
It does not necessarily mean that exactly 60% of the metal surface is covered by inhibitor molecules.
Surface coverage is a separate concept and requires additional assumptions or evidence.
Likewise, a reduction in corrosion current density supports an inhibition effect, but other measurements may be needed to understand the mechanics

Why does the Tafel fitting window matter?
Your notes mention two fitting windows:
50–150 mV
80–200 mV
These are potential offsets from the corrosion potential, but the exact interpretation depends on which branch is being fitted and how the software defines the window.
For example, a cathodic fitting window of 50 –150 mV below Ecorr
corresponds to:
E - Ecorr= -50mV  to  -150mV
An anodic window of 50 –150 mV above Ecorr  corresponds to:
E - Ecorr = +50mV to  +150mV
Why does the choice matter?
Because the Tafel equation is an approximation. Near the corrosion potential, both anodic and cathodic reactions contribute substantially to the net current. Farther away, one reaction may dominate more strongly.
However, moving too far from Ecorr  can introduce other complications, including:
Changes in the reaction mechanism.
Formation or breakdown of surface films.
Diffusion limitations.
Gas bubbles affecting the electrode surface.
Localized corrosion or other nonuniform behaviour.
The ideal fitting region is therefore not simply the farthest region from the corrosion potential.
It is the region where the relevant branch is sufficiently linear and the assumptions behind the Tafel relationship are reasonable.
Why your notes mention 48.0 and 49.7
Your notes state that, for a synthetic test curve:
A 50–150 mV window gave 48.0 μ A/cm2
An 80–200 mV window gave 49.7 μ A/cm2
These values are examples from a simulated curve, not experimental measurements.
The difference is:
49.7−48.0=1.7μA/cm2
Relative to 49.7, the difference is approximately:
49.7-48.049.7 x 100 ≈3.4%
This is broadly consistent with the note’s statement that 48.0 is about 4% lower.
The example demonstrates that changing the fitting window can change the estimated corrosion current density, even when the underlying test curve remains the same.
It does not establish that the 80–200 mV window is always better. That depends on the curve and whether that region genuinely follows Tafel behaviour.

What is the difference between Tafel analysis and Butler–Volmer fitting?
Your notes say that some research groups fit the full Butler–Volmer equation as a cross-check.
Here is the simple distinction.
Tafel analysis fits approximately linear portions of a logarithmic polarization plot.
It relies on selecting suitable anodic and cathodic regions and extrapolating them.
Butler–Volmer fitting uses an equation describing the relationship between current and over potential across a broader range, including regions where both reaction directions contribute significantly.
A full Butler–Volmer fit can be useful when the model appropriately describes the electrochemical system.
However, fitting a more complicated equation does not automatically make the result more accurate. The assumed reaction model must be appropriate, and the parameters must be identifiable from the available data.
For aluminium in acid, surface-film changes or other processes can cause deviations from the simple models. Neither Tafel extrapolation nor Butler–Volmer fitting automatically resolves those complications.
A good researcher compares the model with the measured curve, examines residuals, reports assumptions and avoids claiming more certainty than the data support.






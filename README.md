# Segall-Thrust-2D

A simple coseismic deformation model for a dipping thrust fault, based on Chapter 3 of *Earthquake and Volcano Deformation* by Paul Segall (2010).  
Implements analytic dislocation solutions for plane-strain deformation.


## Equation (3.73): Surface displacements (finite-width fault)

$$
\begin{aligned}
u_1(x_1,0) &= -\frac{s}{\pi} \left( \cos\delta \left[ \tan^{-1}(\zeta) - \tfrac{\pi}{2}\,\mathrm{sgn}(x_1) \right] + \frac{\sin\delta - \zeta\cos\delta}{1+\zeta^2} \right), \\[6pt]
u_2(x_1,0) &= \;\;\frac{s}{\pi} \left( \sin\delta \left[ \tan^{-1}(\zeta) - \tfrac{\pi}{2}\,\mathrm{sgn}(x_1) \right] + \frac{\cos\delta + \zeta\sin\delta}{1+\zeta^2} \right).
\end{aligned}
$$

## Model Description

This implementation evaluates Eq. (3.73) at the ground surface to generate:
- **Horizontal displacement** \(u_1\): motion toward/away from the fault.  
- **Vertical displacement** \(u_2\): uplift or subsidence.  
- **Horizontal strain** \(\varepsilon_{11}\): elastic rebound across the profile. 

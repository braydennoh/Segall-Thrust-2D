# Segall-Thrust-2D

A simple coseismic deformation model for a dipping thrust fault, based on Chapter 3 of *Earthquake and Volcano Deformation* by Paul Segall (2010).  
Implements analytic dislocation solutions for plane-strain deformation.


## Equation (3.73): Surface displacements (finite-width fault)

$$
\begin{aligned}
u_1(x_1,0) &= -\frac{s}{\pi}\Big( \cos\delta \,[ \arctan(\zeta) - \tfrac{\pi}{2}\operatorname{sgn}(x_1) ] + \frac{\sin\delta - \zeta\cos\delta}{1+\zeta^2} \Big),\\[6pt]
u_2(x_1,0) &= \;\;\frac{s}{\pi}\Big( \sin\delta \,[ \arctan(\zeta) - \tfrac{\pi}{2}\operatorname{sgn}(x_1) ] + \frac{\cos\delta + \zeta\sin\delta}{1+\zeta^2} \Big).
\end{aligned}
$$

where

$$
\zeta = \frac{x_1 - x_d}{d}.
$$

## Model Description

This implementation evaluates Eq. (3.73) at the ground surface to generate:
- **Horizontal displacement** \(u_1\): motion toward/away from the fault.  
- **Vertical displacement** \(u_2\): uplift or subsidence.  
- **Horizontal strain** \(\varepsilon_{11}\): elastic rebound across the profile. 

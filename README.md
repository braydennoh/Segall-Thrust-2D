# Segall-Thrust-2D

An elastic dislocation model for a dipping thrust fault, based on Chapter 3 of *Earthquake and Volcano Deformation* by Paul Segall (2010). Implements analytic dislocation solutions for plane-strain deformation.

## Equation (3.70): Surface displacements (buried semi-infinite fault)

This equation calculates the surface displacement from a single, buried edge dislocation whose top is at depth *d*.

$$
\begin{aligned}
u_1(x_1, x_2 = 0) &= \frac{s}{\pi}\Big[ \cos\delta \tan^{-1}(\zeta) + \frac{\sin\delta - \zeta\cos\delta}{1+\zeta^2} \Big], \\
u_2(x_1, x_2 = 0) &= -\frac{s}{\pi}\Big[ \sin\delta \tan^{-1}(\zeta) + \frac{\cos\delta + \zeta\sin\delta}{1+\zeta^2} \Big],
\end{aligned}
$$

where

$$\zeta = \frac{x_1 - \xi_1}{d}.$$

## Equation (3.73): Surface displacements (finite-width, surface-breaking fault)

This equation models a fault that ruptures from the surface down to a depth *d*. 

$$
\begin{aligned}
u_1(x_1,0)&= -\frac{s}{\pi}\Big( \cos\delta \,[ \tan^{-1}(\zeta) - \tfrac{\pi}{2}\,\text{sgn}(x_1) ] + \frac{\sin\delta - \zeta\cos\delta}{1+\zeta^2} \Big), \\
u_2(x_1,0)&= \frac{s}{\pi}\Big( \sin\delta \,[ \tan^{-1}(\zeta) - \tfrac{\pi}{2}\,\text{sgn}(x_1) ] + \frac{\cos\delta + \zeta\sin\delta}{1+\zeta^2} \Big).
\end{aligned}
$$

where

$$\zeta = \frac{x_1 - x_d}{d}.$$

This implementation evaluates these equations at the ground surface to generate:
- **Horizontal displacement** ($u_1$): motion toward/away from the fault. 
- **Vertical displacement** ($u_2$): uplift or subsidence. 
- **Horizontal strain** ($\varepsilon_{11}$): elastic rebound across the profile.


<img src="https://github.com/braydennoh/Segall-Thrust-2D/blob/main/image/segallmcmc.png">

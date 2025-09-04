# Segall-Thrust-2D

A simple coseismic deformation model for a dipping thrust fault, based on Chapter 3 of *Earthquake and Volcano Deformation* by Paul Segall (2010).  
Implements analytic dislocation solutions for plane-strain deformation.

---

## Equations

### (3.70) Surface displacements (infinite fault)
\[
\begin{aligned}
u_1(x_1,0) &= \frac{s}{\pi} \left[ \cos\delta \,\tan^{-1}(\zeta) + \frac{\sin\delta - \zeta\cos\delta}{1+\zeta^2} \right], \\
u_2(x_1,0) &= -\frac{s}{\pi} \left[ \sin\delta \,\tan^{-1}(\zeta) + \frac{\cos\delta + \zeta\sin\delta}{1+\zeta^2} \right].
\end{aligned}
\]

### (3.71) Dimensionless coordinate
\[
\zeta = \frac{x_1 - \xi_1}{d}
\]

### (3.72) Horizontal strain
\[
\varepsilon_{11}(x_1,0) = \frac{\partial u_1}{\partial x_1}
= \frac{2s}{\pi d} \cdot \frac{\zeta^2 \cos\delta - \zeta\sin\delta}{(1+\zeta^2)^2}
\]

### (3.73) Surface displacements (finite-width fault)
\[
\begin{aligned}
u_1(x_1,0) &= -\frac{s}{\pi} \left\{ \cos\delta \left[ \tan^{-1}(\zeta) - \tfrac{\pi}{2}\,\mathrm{sgn}(x_1) \right] + \frac{\sin\delta - \zeta\cos\delta}{1+\zeta^2} \right\}, \\
u_2(x_1,0) &= \;\;\frac{s}{\pi} \left\{ \sin\delta \left[ \tan^{-1}(\zeta) - \tfrac{\pi}{2}\,\mathrm{sgn}(x_1) \right] + \frac{\cos\delta + \zeta\sin\delta}{1+\zeta^2} \right\}.
\end{aligned}
\]

---

## Model

This implementation evaluates Eq. (3.73) at the ground surface to generate:
- **Horizontal displacement** \(u_1\): motion toward/away from the fault.
- **Vertical displacement** \(u_2\): uplift or subsidence.
- **Horizontal strain** \(\varepsilon_{11}\): elastic rebound across the profile.

The output reproduces the typical deformation from large subduction thrust earthquakes:  
uplift at the trench, subsidence over the downdip end, and extensional strain with small compressional zones.

---

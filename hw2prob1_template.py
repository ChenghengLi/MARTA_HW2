# (c) 2023 Michael Fitzgerald (mpfitz@ucla.edu)
#
# Some code for computing some aspects of Keplerian orbits.  Students are expected to re-organize this code and do some eample calculations
#
#


import numpy as np


# -----------------------------
# The following blocks of code are useful for calculating some aspects of Keplering orbits.  However, they are not currently usable.  You should move this code to a module, and wrap them in function definitions.
#


# Solves Kepler's equation, returning eccentric anomaly E given M, e.
#       M = E - e*sin(E)
# mean anomaly (M) expected as array,  eccentricity (e) expected as scalar
from scipy.optimize import fmin
kep = lambda E, M: np.sum(np.abs(M-E+e*np.sin(E)))
E0 = M + np.sign(np.sin(M)) * 0.85 * e # initial guess
E = np.empty_like(M)
for i, M in enumerate(M):
    E[i] = fmin(kep, E0[i], args=(M,),
                disp=False,
                )


# solves for the space position of an object in a Keplerian orbit given:
#    a      semimajor axis [AU]
#    e      eccentricity
#    inc    inclination [rad]
#    omega  argument of periastron [rad]
#    Omega  longitude of ascending node [rad]  relative to x axis, counterclockwise
#    M      mean anomaly [rad]
# Below the variables x, y, z are space position [AU]

# compute eccentric anomaly
E = ???????(M, e) # [rad] eccentric anomaly found by solving kepler's equation

# compute true anomaly
nu = 2.*np.arctan2(np.sqrt(1.+e)*np.sin(E/2.), np.sqrt(1.-e)*np.cos(E/2.)) # [rad]

# compute radius
r = a * (1.-e**2) / (1.+e*np.cos(nu)) # [AU]

# compute various sin/cos factors
so, co = np.sin(omega), np.cos(omega)
sonu, conu = np.sin(omega+nu), np.cos(omega+nu)
sO, cO = np.sin(Omega), np.cos(Omega)
si, ci = np.sin(inc), np.cos(inc)

# compute space position
x = r * (cO*conu-sO*sonu*ci) # [AU]
y = r * (sO*conu+cO*sonu*ci) # [AU]
z = r * sonu*si

# end of code snippets for Keplerian calculations
# -----------------------------



# parameters in order are:
#    a      semimajor axis [AU]
#    e      eccentricity
#    inc    inclination [rad]
#    omega  argument of periastron [rad]
#    Omega  longitude of ascending node [rad]  relative to x axis, counterclockwise
#    T      period [days]
#    T0     time of periastron [days]
# Keplerian parameters for object 1
obj1parms = (10., 0.02, 70. * np.pi/180., 20. * np.pi/180., -15. * np.pi/180., 30. * 365.25, 1.88)
# Keplerian parameters for object 2
obj2parms = (15., 0.3, 85. * np.pi/180., 15. * np.pi/180., 5. * np.pi/180., 55. * 365.25, 8.66)
# Note, normally the period of the objects would be directly related to the semimajor axis, given the mass of the central star.  Here I am just making up parameters.

# how to compute mean anomaly from t, T, and T0
# make this a function
M = (t-T0)/T * 2.*np.pi # [rad]  mean anomaly


# compute the positions of objects 1 and 2 every 10 days until object 2 begins to reverse direction along the line of sight (z axis).



# plot the positions of the objects

# save the plot to PDF

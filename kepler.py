# This is a module file to X

import numpy as np
from scipy.optimize import fmin

# mean anomaly (M) expected as array,  eccentricity (e) expected as scalar
# M = E - e*sin(E)


def solve_Kepler(M, e):
    """ Solves Kepler's equation, returning eccentric anomaly E in [rad] given M, e."""
    kep = lambda E, M: np.sum(np.abs(M-E+e*np.sin(E)))
    E0 = M + np.sign(np.sin(M)) * 0.85 * e # initial guess
    E = np.empty_like(M)
    for i, M in enumerate(M):
        E[i] = fmin(kep, E0[i], args=(M,),
                    disp=False,
                    )
    return E


# compute true anomaly
def find_True_Anomaly(E, e):
    nu = 2.*np.arctan2(np.sqrt(1.+e)*np.sin(E/2.), np.sqrt(1.-e)*np.cos(E/2.)) # [rad]
    return nu

# find space positions (radius, sin/cos factors)

def find_Space_Positions(a, e, inc, omega, Omega, nu):
    r = a * (1.-e**2) / (1.+e*np.cos(nu)) # compute radius [AU]
    so, co = np.sin(omega), np.cos(omega) # compute various sin/cos factors
    sonu, conu = np.sin(omega+nu), np.cos(omega+nu)
    sO, cO = np.sin(Omega), np.cos(Omega)
    si, ci = np.sin(inc), np.cos(inc)
    x = r * (cO*conu-sO*sonu*ci) # [AU]
    y = r * (sO*conu+cO*sonu*ci) # [AU]
    z = r * sonu*si
    return x, y, z
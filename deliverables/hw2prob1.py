import numpy as np
import kepler # Import the kepler module
import matplotlib.pyplot as plt

# Define Keplerian parameters for object 1 and object 2
# parameters in order are:
#    a      semimajor axis [AU]
#    e      eccentricity
#    inc    inclination [rad]
#    omega  argument of periastron [rad]
#    Omega  longitude of ascending node [rad]  relative to x axis, counterclockwise
#    T      period [days]
#    T0     time of periastron [days]

obj1parms = (10., 0.02, 70. * np.pi/180., 20. * np.pi/180., -15. * np.pi/180., 30. * 365.25, 1.88)
obj2parms = (15., 0.3, 85. * np.pi/180., 15. * np.pi/180., 5. * np.pi/180., 55. * 365.25, 8.66)

# Find Mean Anomaly, given the period T [days] and the time of periastron T0 [days].
def find_Mean_Anomaly(t,T,T0):
    M = (t-T0)/T * 2.*np.pi # [rad]  mean anomaly
    return M

# Define time intervals
t_init = 0
t_final = 365*100 # 100 years
t_step = 10
t_intervals = np.arange(t_init, t_final, t_step) # array of time values at regular intervals

# Compute the positions of objects 1 and 2 every 10 days until object 2 begins to reverse direction along the line of sight (z axis).

M1 = find_Mean_Anomaly(t_intervals, obj1parms[5], obj1parms[6])
M2 = find_Mean_Anomaly(t_intervals, obj2parms[5], obj2parms[6])
E1 = kepler.solve_Kepler(M1, obj1parms[1])
E2 = kepler.solve_Kepler(M2, obj2parms[1])
nu1 = kepler.find_True_Anomaly(E1, obj1parms[1])
nu2 = kepler.find_True_Anomaly(E2, obj2parms[1])
x1, y1, z1 = kepler.find_Space_Positions(obj1parms[0], obj1parms[1], obj1parms[2], obj1parms[3], obj1parms[4], nu1)
x2, y2, z2 = kepler.find_Space_Positions(obj2parms[0], obj2parms[1], obj2parms[2], obj2parms[3], obj2parms[4], nu2)


# Plot the positions of the objects

plt.scatter(x1, y1, label='Object 1')
plt.scatter(x2, y2, label='Object 2')
plt.title("HW2 EX1")
plt.xlabel('X Position')
plt.ylabel('Y Position')


# Save the plot to PDF
plt.savefig("HW2PROB1_image.pdf", format="pdf", bbox_inches="tight")

print("Done!")
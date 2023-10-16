
import numpy as np
import kepler # Import the kepler module
import matplotlib as plt


# parameters in order are:
#    a      semimajor axis [AU]
#    e      eccentricity
#    inc    inclination [rad]
#    omega  argument of periastron [rad]
#    Omega  longitude of ascending node [rad]  relative to x axis, counterclockwise
#    T      period [days]
#    T0     time of periastron [days]

# Define Keplerian parameters for object 1 and object 2
obj1parms = (10., 0.02, 70. * np.pi/180., 20. * np.pi/180., -15. * np.pi/180., 30. * 365.25, 1.88)
obj2parms = (15., 0.3, 85. * np.pi/180., 15. * np.pi/180., 5. * np.pi/180., 55. * 365.25, 8.66)

# Find Mean Anomaly from time parameters
def find_Mean_Anomaly(t,T,T0):
    M = (t-T0)/T * 2.*np.pi # [rad]  mean anomaly
    print(M)
    return M


# Define time intervals
t_init = 0
t_final = 365240 # 100 years
t_step = 10
t_intervals = np.arange(t_init, t_final, t_step) # array of time values at regular intervals

# compute the positions of objects 1 and 2 every 10 days until object 2 begins to reverse direction along the line of sight (z axis).

x1_positions, y1_positions = [], []  # For object 1
x2_positions, y2_positions = [], []  # For object 2


for t in t_intervals:
    # Find the mean anomaly for object 1 and object 2
    M1 = find_Mean_Anomaly(t, obj1parms[5], obj1parms[6])
    M2 = find_Mean_Anomaly(t, obj2parms[5], obj2parms[6])
    E1 = kepler.solve_Kepler(M1, obj1parms[1])
    E2 = kepler.solve_Kepler(M2, obj2parms[1])
    nu1 = kepler.find_True_Anomaly(E1, obj1parms[1])
    nu2 = kepler.find_True_Anomaly(E2, obj2parms[1])
    x1, y1, z1 = kepler.find_Space_Positions(obj1parms[0], obj1parms[1], obj1parms[2], obj1parms[3], obj1parms[4], nu1)
    x2, y2, z2 = kepler.find_Space_Positions(obj2parms[0], obj2parms[1], obj2parms[2], obj2parms[3], obj2parms[4], nu2)
    x1_positions.append(x1)
    y1_positions.append(y1)
    x2_positions.append(x2)
    y2_positions.append(y2)

# plot the positions of the objects

plt.scatter(x1_positions, y1_positions, label='Object 1')
# Create a scatter plot for object 2 (x, y positions)
plt.scatter(x2_positions, y2_positions, label='Object 2')
plt.xlabel('X Position')
plt.ylabel('Y Position')
plt.show()

# save the plot to PDF



M1 = find_Mean_Anomaly(t_intervals, obj1parms[5], obj1parms[6])


E1 = kepler.solve_Kepler(M1, obj1parms[1])
print(t_intervals)

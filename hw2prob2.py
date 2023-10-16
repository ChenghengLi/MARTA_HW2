# A few problems in defining data models with numpy.  Demonstrates building complex
# data tpyes and subclassing numpy arrays to add metadata.

import numpy as np
import matplotlib.pyplot as plt

# Problem 2a
# Time-series photometry with irregular spacing. Here, we’re monitoring the received flux of a source 
# (expressed in Jy) at irregularly spaced time intervals (expressed in MJD).
photometry_dtype = np.dtype([('time', float), ('flux', float)])
np.random.seed(0)
random_time = np.sort(np.random.uniform(0,60,60)) # 60 time measurements during 60 seconds at random irregular spacing.
random_flux = np.random.randn(60) 

photometry_data = np.array([random_time, random_flux], dtype=photometry_dtype) # instance

print("Time values, in MJD:", photometry_data['time']) 
print("Flux values, in Jy:", photometry_data['flux'])


# Problem 2b
# Time-series spectroscopy, obtained at regular intervals.
# Here, at each regularly spaced timestep (in MJD), we record a spectrum (in Jy) at evenly spaced wavelength 
# intervals. Spectra obtained at different times all have the same wavelength grid.  
# Consider defining the regularly spaced wavelength grid as metadata.  Be sure to be able to recover 
# the timestamp of each spectrum – this may be done by recording the t0 and delta t as metadata.

class SpectroscopyData_regular:
    def __init__(self, time, spectrum, wv_grid, t0, delta_t):
        self.time = time
        self.spectrum = spectrum
        self.wv_grid = wv_grid
        self.t0 = t0
        self.delta_t = delta_t


# Instance of time-series spectroscopy at regular intervals.


# Problem 2c
# Time-series spectroscopy, with irregular intervals.  
# Spectra are obtained at different times, and with different wavelength grids.  
# Each spectrum may have a unique length (number of elements).


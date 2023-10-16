# A few problems in defining data models with numpy.  Demonstrates building complex
# data tpyes and subclassing numpy arrays to add metadata.

import numpy as np
import matplotlib.pyplot as plt

# Problem 2a
# Time-series photometry with irregular spacing. Here, we’re monitoring the received flux of a source 
# (expressed in Jy) at irregularly spaced time intervals (expressed in MJD).
photometry_dtype = np.dtype([('time', np.float64), ('flux', np.float64)])
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

# Define a subclass of a numpy array that has additional metadata accessible as an attribute
class Spectrocopy(np.ndarray):
    def __new__(subtype, shape, dtype=float, buffer=None, offset=0, strides=None, order=None, info=None):
        obj = super().__new__(subtype, shape, dtype, buffer, offset, strides, order)
        obj.info = info
        return obj

    def __array_finalize__(self, obj):
        if obj is None: return
        self.info = getattr(obj, 'info', None)


# Define the data type
RegularSpectrocopy_dtype = np.dtype([('time', np.float64), ('spectrum', np.float64, (10,))], metadata={'unit_time': 'MJD', 'unit_spectrum': 'Jy'})

# Create an array of zeros with the defined data type
RegularSpectroscopy_data = np.zeros((60,), dtype=RegularSpectrocopy_dtype)

# Generate regularly spaced time intervals and random spectrum values
RegularSpectroscopy_data['time'] = np.linspace(0, 100, 60)
RegularSpectroscopy_data['spectrum'] = np.random.uniform(0, 10, (60, 10)) # Each spectrum has a fixed number of elements (10) with a random value between 0 and 10

# Define the regularly spaced wavelength grid
wavelength_grid = np.linspace(0, 1, 10)

# Create an instance of Spectroscopy with the array and metadata
RegularSpectroscopy_instance = Spectrocopy(shape=RegularSpectroscopy_data.shape, buffer=RegularSpectroscopy_data, info={'description': 'Time-series spectroscopy with regular intervals', 'wavelength_grid': wavelength_grid, 't0': RegularSpectroscopy_data['time'][0], 'delta_t': RegularSpectroscopy_data['time'][1] - RegularSpectroscopy_data['time'][0]})

# Print the array and metadata

print('Time values, in MJD:', RegularSpectroscopy_instance['time']) 
print('Flux values, in Jy:', RegularSpectroscopy_instance['flux'])
print('Metadata:', RegularSpectroscopy_instance.info)


# Problem 2c
# Time-series spectroscopy, with irregular intervals.
# Spectra are obtained at different times, and with different wavelength grids.
# Each spectrum may have a unique length (number of elements).

# Define the data type
IrregularSpectroscopy_dtype = np.dtype([('time', np.float64), ('spectrum', np.float64)], metadata={'unit_time': 'MJD', 'unit_spectrum': 'Jy'})

# Create an array of zeros with the defined data type
IrregularSpectroscopy_data = np.zeros((60,), dtype=IrregularSpectroscopy_dtype)

# Generate irregularly spaced time intervals and random spectrum values with different lengths
IrregularSpectroscopy_data['time'] = np.sort(np.random.uniform(0, 100, 60))
for i in range(60):
    IrregularSpectroscopy_data['spectrum'][i] = np.random.uniform(0, 10, np.random.randint(1, 11)) # Each spectrum has a random number of elements between 1 and 10 with a random value between 0 and 10 

# Create an instance of Spectroscopy with the array and metadata
IrregularSpectroscopy_instance = Spectrocopy(shape=IrregularSpectroscopy_data.shape, buffer=IrregularSpectroscopy_data, info={'description': 'Time-series spectroscopy with irregular intervals'})

# Print the array and metadata

print('Time values, in MJD:', IrregularSpectroscopy_instance['time']) 
print('Flux values, in Jy:', IrregularSpectroscopy_instance['flux'])
print('Metadata:', IrregularSpectroscopy_instance.info)

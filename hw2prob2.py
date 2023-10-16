# A few problems in defining data models with numpy.  Demonstrates building complex
# data tpyes and subclassing numpy arrays to add metadata.
#

import numpy as np

# This is an example for how to define a subclass of a numpy array that has additional metadata accessible as an attribute.  We can set the 'info' attribute either at construction or later.
# Example code derived from the numpy manual:  https://numpy.org/doc/stable/user/basics.subclassing.html#simple-example-adding-an-extra-attribute-to-ndarray
class InfoArray(np.ndarray):

    def __new__(subtype, shape, dtype=float, buffer=None, offset=0, strides=None, order=None, # these are all required arguments for numpy array construction
                info=None, # this is our additional metadata
                ):
        # Create the ndarray instance of our type, given the usual
        # ndarray input arguments.  This will call the standard
        # ndarray constructor, but return an object of our type.
        # It also triggers a call to InfoArray.__array_finalize__
        obj = super().__new__(subtype, shape, dtype,
                              buffer, offset, strides, order)

        # set the new 'info' attribute to the value passed
        obj.info = info
        
        return obj # return the newly created object

    def __array_finalize__(self, obj):
        # ``self`` is a new object resulting from
        # ndarray.__new__(InfoArray, ...), therefore it only has
        # attributes that the ndarray.__new__ constructor gave it -
        # i.e. those of a standard ndarray.
        #
        # We could have got to the ndarray.__new__ call in 3 ways:
        # From an explicit constructor - e.g. InfoArray():
        #    obj is None
        #    (we're in the middle of the InfoArray.__new__
        #    constructor, and self.info will be set when we return to
        #    InfoArray.__new__)
        if obj is None: return
        # From view casting - e.g arr.view(InfoArray):
        #    obj is arr
        #    (type(obj) can be InfoArray)
        # From new-from-template - e.g infoarr[:3]
        #    type(obj) is InfoArray


        # Note that it is here, rather than in the __new__ method,
        # that we set the default value for 'info', because this
        # method sees all creation of default objects - with the
        # InfoArray.__new__ constructor, but also with
        # arr.view(InfoArray).
        self.info = getattr(obj, 'info', None)

# demonstrating the functionality of this subclass:
#
n_val = 3
test1 = InfoArray(shape=(n_val,))
test1[:] = np.arange(n_val) # set all values of the array.  Note if we had done test1 = ... we would no longer have test1 be an InfoArray.
print('Here are the array values:')
print(test1)
print(test1.info is None) # should be True
test1.info = 'This is extra information' # adding metadata after instantiation
print(test1.info)
test2 = InfoArray(shape=(3,), info='so is this!') # adding metadata during construction
print(test2.info)


# You may wish to refer to https://numpy.org/doc/stable/user/basics.rec.html for building complex dtypes in numpy.

# For each case, write code to define the dtype and/or class.  Then, create an instance of such arrays of data to demonstrate functionality.

# Problem 2a
# Time-series photometry with irregular spacing.  
# Here, we’re monitoring the received flux of a source (expressed in Jy) at irregularly spaced time intervals (expressed in MJD).
photometry_dtype = np.dtype([('time', float), ('flux', float)])
photometry_data = np.array([(2459000.0, 1.23), (2459001.5, 2.45)], dtype=photometry_dtype) # instance

print("Time values, in MJD:", photometry_data['time'])
print("Flux values, in Jy:", photometry_data['flux'])


# Problem 2b
# Time-series spectroscopy, obtained at regular intervals.
# Here, at each regularly spaced timestep (in MJD), we record a spectrum (in Jy) at evenly spaced wavelength intervals.  
# Spectra obtained at different times all have the same wavelength grid.  
# Consider defining the regularly spaced wavelength grid as metadata.  Be sure to be able to recover the timestamp of each spectrum – this may be done by recording the t0 and delta t as metadata.

class SpectroscopyData_regular:
    def __init__(self, time, spectrum, wv_grid, t0, delta_t):
        self.time = time
        self.spectrum = spectrum
        self.wv_grid = wv_grid
        self.t0 = t0
        self.delta_t = delta_t

# Instance of time-series spectroscopy at regular intervals.
#

# Problem 2c
# Time-series spectroscopy, with irregular intervals.  
# Spectra are obtained at different times, and with different wavelength grids.  
# Each spectrum may have a unique length (number of elements).

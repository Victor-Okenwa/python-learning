import numpy as np

matrix = np.array([
    [1, 2, 3, 4],
    [5, 6, 7, 8]
])

print( matrix.shape)
print( "size: ", matrix.size)
print( "ndim: ", matrix.ndim)
print( "dtype: ", matrix.dtype)
print( "itemsize: ", matrix.itemsize)
print( "nbytes: ", matrix.nbytes)
print( "strides: ", matrix.strides)
print( "flags: ", matrix.flags)
print( "real: ", matrix.real)
print( "imag: ", matrix.imag)
print( "flat: ", matrix.flat)
print( "flatten: ", matrix.flatten())


import numpy as np

a2 = np.empty((3,3))
print("2D array", +a2)
a3 = np.empty((3,3,3))
print("3D array", +a3)
min = a3.min()
print("min is:", +min)
max = a3.max()
print("max is:", +max)
reshaped = a3.reshape((-1,9))
print("reshaped array", +reshaped)
reshaped2 = a3.reshape((-1,3))
print("reshaped array again", +reshaped2)
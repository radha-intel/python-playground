import numpy as np
import csv
import pandas as pd

a1 = np.random.rand(3,3)
print(a1)
a11 = np.random.rand(3,3,3)
print(a11)
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
restored = reshaped2.reshape(3,3,3)
print("Restored 3D array", +restored)
data = pd.read_csv('data.csv').values
#data = data.to_numpy()
print("data from .csv file", +data)
print(type(data))
print(data[15479][2])
#data = np.genfromtxt('data.csv', delimiter=',')
#res = data[:,1]
#res = data[:,0:2]
#print(data)
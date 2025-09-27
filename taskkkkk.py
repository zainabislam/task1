import numpy as np
a=np.array([10,20,30,40,50])
b=np.array([5,4,3,2,1])
print(a + b)
print(a - b)
print(a * b)
print(a / b)

print(a.min())
print(a.max())

print(a.sum() /a.shape) #mean

reshaped_a=a.reshape(5,1)
print(reshaped_a)
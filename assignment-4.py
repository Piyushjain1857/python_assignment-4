# Q1. Explain the key features of NumPy and highlight the major differences between NumPy arrays and Python lists with appropriate examples.

'''Ans:- NumPy is a multy dimensional arrey object which can efficienty store and manuplate data easily.It have many build-in functions such as indexing,slicing,mathametical,statistical,etc functions. It can perform slicing without using the loops. It also have a powerfull mechanism that can perform on arrays of different shapes and sizes'''

'''Ans:- Differcence Between NumPy and List :--
1) The NumPy arreys are 50x faster then the lists.
2) NumPy arreys can stores only hetrogenious data type where as the list stores homogenious data.
3) NumPy uses less memory where as lists uses more memory.
4) NumPy can perform direct element operations whereas in lists we have to use loops to perform any operation.
5) NumPy is multi-dimensional whereas list is only one-dimensional.
6) NumPy supports Broadcasting whereas lists don't support it. '''

# Example:-

import numpy as np

# NumPy array
arr1 = np.array([1, 2, 3])
print(arr1*2)

# Python list
l = [1, 2, 3]
l2=[]
for i in range(len(l)):
    x= l[i]*2
    l2.append(x)
print(l2)


# Q2. Develop a Python program using NumPy to create one-dimensional and two-dimensional arrays, and display their shape, dimensions, and data type.


# One-dimensional array
arr1 = np.array([1,2,3,4,5])
print(f"One-D Array:-{arr1}")
print(f"Shape:-{arr1.shape}")
print(f"Dimensions:-{arr1.ndim}")
print(f"Data type:-{arr1.dtype}")

# Two-dimensional array
arr2 = np.array([[1, 2, 3], [4, 5, 6]])
print(f"2D Array:-{arr2}")
print(f"Shape:-{arr2.shape}")
print(f"Dimensions:-{arr2.ndim}")
print(f"Data type:-{arr2.dtype}")

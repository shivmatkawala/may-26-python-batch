# Numpy:-
    # Numeric  Python
    # Open Source
    # Numpy is the fundamental library for scientific computing
    # in python. It provides
        # Fast Multidiamensional Array.
        # Mathematical Operations
        # Linear Algebra
        # Statistical Functions
        # Random Number Generation
        # Broadcasting
        # Itegration with data science libraries, dat engineering Libraries
            # Pandas, SciPy, Sckit-learn

# Import numpy module in file where you want to use it.

import numpy as np


# Using numpy create an array:

# ar1 = np.array((1, 2, 3, 4, 5))
# print(ar1)

# ar2 = np.array([1, 2, 3, 4, 5])
# print(ar2)

#---------------------
# some attributes

# shape

# l1 = [1, 2, 3, 4, 5, 6]   # linear , 1 diamensional

# l2 = [[1, 2], [3, 4], [5, 6]] # non-linear. 2 ddiamensiaonal

# l3 = [
#     [
#         [1, 2, 3],
#         [4, 5, 6]
#     ],
#     [
#         [7, 8, 9],
#         [10, 11, 12]
#     ]
# ]

#------------------------

# names = np.array(["Alan", "sara", "Jaya"])
# ages = np.array([34, 32, 25])
# salary = np.array([50000, 60000, 100000])
# positions = np.array(["JD", "JD", "SD"])


#----------------------------
# ndim
# arr1 = np.array([1, 2, 3, 4, 5])
# print(arr1.ndim)  #1

# arr2 = np.array([
#     [1, 2, 3],
#     [4, 5, 6]
# ])

# print(arr2.ndim)

# arr3 = np.array([
#     [
#         [1, 2, 3],
#         [4, 5, 6]
#     ],
#     [
#         [7, 8, 9],
#         [10, 11, 12]
#     ]
# ])

# print(arr3.ndim)

#-------------------
#size

# arr100 = np.array([1, 2, 3, 4, 5])
# print(arr100.size)

# arr200 = np.array([
#     [1, 2, 3],
#     [4, 5, 6]
# ])

# print(arr200.size)

#-----------------------
# dtype

# ar1 = np.array([1, 2, 3, 4])
# print(ar1.dtype)   #int64

# ar2 = np.array(["A", "B", "C"])
# print(ar2.dtype)


#--------------------------------
# Creating Arrays:

# zeros

# zeros1 = np.zeros((2, 3))
# print(zeros1)


# zeros2 = np.zeros((6, 10))
# print(zeros2)


# ones
# ones1 = np.ones((3, 3))
# print(ones1)

# ones2 = np.ones((8, 5))
# print(ones2)


#--------------------------
# Full

# full1 = np.full((2,2),  7)
# print(full1)

# full2 = np.full((5, 3), 10)
# print(full2)

#--------------------
# Identity Matrix:

# eye

# identity1 = np.eye(6)
# print(identity1)

# identity2 = np.eye(3)
# print(identity2)

#-------------------------------

# Evenly spaced values:
# linspace

# ar1 = np.linspace(1, 10, 5)
# print(ar1)

# ar2 = np.linspace(0, 5, 100)
# print(ar2)

#---------------------------

# ar1 = np.array([1, 2, 3, 4, 5], dtype=complex)
# print(ar1)
# print(ar1.dtype)

# ar2 = np.array([1+2j, 3+4j, 5+6j], dtype=int)
# print(ar2)
# print(ar2.dtype)


# ar3 = np.array(["1", "2", "3", "4"], dtype=int)
# print(ar3)
# print(ar3.dtype)


#-----------------------------
# Indexing:
# arr1 = np.array([10, 20, 30, 40, 50])
# print(arr1)
# print(arr1[0])
# print(arr1[4])

# print(arr1[-1])
# print(arr1[-3])


#-------------------------------
# Slicing:

# arr2 = np.array([12, 23, 34, 45, 56, 67])
# print(type(arr2[1:4:1]))


#--------------------------------
# 2D Arrays:

# a1 = np.array([
#     [1, 2, 3], 
#     [4, 5, 6],
#     [7, 8, 9]
# ])

# print(a1[1][1])  # simple python like
# print(a1[1, 1])  # numpy like answer

#--------------------------
# print(a1[2])
# print(a1[:,0])

#-------------------------
# Array Operations:

# a1 = np.array([1, 2, 3])
# a2 = np.array([4, 5, 6])

# print(a1+a2)
# print(a1 - a2)
# print(a1 * a2)
# print(a1 / a2)

#------------------------
# aa1 = np.array([1, 2, 3])
# z = 10

# print(aa1 + z)

#-------------------------
# Universal Funcions:
ar1 = np.array([1, 4, 9, 16])
# print(np.sqrt(ar1).dtype)


#------------------------------
# print(np.sin(ar1))
# print(np.cos(ar1))
# print(np.log(ar1))

# print(np.min(ar1))
# print(np.max(ar1))
# print(np.sum(ar1))
# print(np.prod(ar1))
# print(np.std(ar1))

# import statistics
# l1 = [1, 7, 2, 0, 5, 0]
# print(statistics.median(l1))
# print(statistics.mode(l1))

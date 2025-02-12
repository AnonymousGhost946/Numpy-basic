# 7-2-25

# today we study about array attribues.

# we cover ndim, shape, size and dtype

# first import numpy
import numpy as np

# now we make a multidimensional array that's the reason we first study single and multidimensional array.

myArray = np.array([
    [1, 2, 3, 4],
    [5, 6,7,8]  # Remember the element length in dimensional array for each dimension must be same otherwise it give us error. If you delete one element form second dimension then it will give use erro. Remove 8  or any else like this  [5,6,7,] now we have three run your code. You will see it give us error
])

# our first attribute is ndim
# ndim tell us the number of dimension  of an array . as we know its 2 dimensional array let see what it tell us

print(myArray.ndim) #it will tell use how much dimension we have in array  outpu : 2

# next we have shape 
# shape tell us two thing fisrt how  much dimension and the length of each dimension element 
print(myArray.shape) # outpu : (2,4)

# next we have size 
# size tell us the total length of elements in all dimensions
print(myArray.size) #output 8

# next we have dtype mean data type
# it tell us which data type of elements we have

print(myArray.dtype) #output :   int64  int stand for integer and 64    stand for 64 bit




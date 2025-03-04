# In this file we review our previous lesson  one by one mean learn the major things that help us in real life or recommended by people.

# One thing we might not discuss before and that is numpy is the base of pandas and pytorch

# if we spend more time to learn numpy then we can learn panda and pytorch three time faster.

# lets start 

# first to make a simple numpy array 

import numpy as np


myArray=np.array([
    [1,2,3,4,5],
    [6,7,8,9,10]    
    ])
print(myArray[1][1])

# now we use slice and make a sliceArray with element 6,7,8,9

sliceArray=myArray[1][:4]
print("sliced array is : \n",sliceArray)

# now we use reshpes to make sliceArray a array 

reshapeArray=sliceArray.reshape(2,2)
print("Reshape array is  below\n",reshapeArray)

# now we make array with the help of range feature

rangeArray=np.arange(8)
print(rangeArray)

print("\n flatten and ravel and their difference \n")

# next we create a multidimensional array and then convert it single array witht the help of flatten

multiArray=np.array([
    [1,2,3,4,5],
    [6,7,8,9,10],
    [11,12,13,14,15]
])
#now we convert it single array with the help of flatten

flattenArray=multiArray.flatten()
print("with flatten() : ",flattenArray)

# now we do same thing with the help of ravel() and then see what the difference is

ravelArray= multiArray.ravel()
print(ravelArray)


print("\n difference between flatten and ravel \n")

# now we tell what the difference between ravel and flatten
# for that difference we have to add or replace element in flatten array and ravelArray. And then we have to print original array mean multiArray

# first we make changes in flattenArray
flattenArray[1]=33
print("new flattenArray", flattenArray)
# now we make changes in ravelArray 

ravelArray[1]=44
print("new ravelArray : " ,ravelArray)

# now we print multiArray to seem which one make view and which one make copy of original array 

print(multiArray)

# as we can see ravel create view of array and flatten make copy of array .
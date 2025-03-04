# 17- 2 - 25
# topic Index and slicing 
# today we learn about indexing and slicing. we already give it a small touch. But now we clear our issue and get more familiar with it


# if you read the 02-list-slice and 03 file then you have a good knowledge that help us here also or we are discussing it again but with  a little bit more discussion.

# or if you familair with list slicing then it is also the same thing in numpy array

# sliceArray=myArray[0:2]  this method is called slicing and indexing of array. see practical examples below.

import numpy as np

#create simple array 
myArray=np.array(["one","two", "three", "four"]) # data type of all elements should must be same

#printing myArray
print(myArray)

# what is slice?
# In simple making array from and existing array is known as slicing


# now we make a sliceArray with the help of slicing from and existing array myArray

sliceArray=myArray[:2]  # as you can see we no mention it where to start and by default it start from  0 so it start form 0 and fo up to 3rd element but the last element will not include 

print(sliceArray) # output ['one', 'two']

# now we are going to make one more slice array but this time we not give the end value

sliceArray2=myArray[1:] # here we not defing it end value then by default it goes to the last index. And we tell it start form 1 . Rememeber in programming languages counting start form 0 not 1 . so in actual 1 is 2 
print(sliceArray2) # ouput  ['two' 'three' 'four']

#  Yout Task is to give negative value and see what happend in counting start form 0 and if we use negative value then it start from which side




# Now we are going to perform some mathematical action with array

myArray2=np.array([
    [1,2,3,4,5],
    [6,7,8,9,10],
    [11,12,13,14,15]
])

# now we are going to print only those values the are below then 7

# boolean indexing

# the below condition is called boolean indexing . Mean  we tell the condition and that condiiton make a boolean ouput whether it is true of false. 
print(myArray2[myArray2 < 7]) # in output you see everything come in 1 dimensional array because it by default use flatten and convert our array.  we already study flatten in 09reshapes.py


# we can also perform division on it 

division_Array= myArray2[myArray2%2==0]
print("Element divisioble by 2 are : " , division_Array)

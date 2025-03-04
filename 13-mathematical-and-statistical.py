# 23 - 2 - 25

# In this tutorial we are going to perform some built in mathematics fearutres of numpy array 

#first we study about statistical operations
#np.min , np.max , np.median , np.mean
import numpy as np

myarr=np.array([1,2,3,4,5,6])
print("Our original array is : ",myarr) #Our original array is :  [1 2 3 4 5 6]

#now first we have np.min() and max. It tell us the lowest and largest value
minArray=np.min(myarr)
print("min value is : ",minArray)
maxArray=np.max(myarr)
print("max value is : ",maxArray)

# next we have np.median
# median is the middle value of the stored data in float. Mean in our original array our middel value is 3.5

medianArray=np.median(myarr)
print("median array is :" ,medianArray)

# next we have np.mean
# mean give us the average
# to get a good reslu change the array add some more values in array 
# we add some more element with the help of append

myarr=np.append(myarr, 21)
# and if we want to add multiple element then we use do like this mean we pass a small array . See below

myarr=np.append(myarr,[24,25,26])
print(myarr) # output  [ 1  2  3  4  5  6 21 24 25 26]

# using mean
averageArray=np.mean(myarr)
print(averageArray) # output            11.7 average 

# next we have np.std  honestly i don't know what this do something related with mean. I also do research I am also student and I don't find any good answer or maybe I not understand it. But if you have a simple answer then please share it with me also.


# i know we have to discuss some math features but no here in next file. Because I think its a little bit complex.

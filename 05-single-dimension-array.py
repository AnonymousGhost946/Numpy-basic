# 6 -2 -25
# today our topic is single dimension array 

# a single or 1 dimensional array (1D array) in python is  a collection of elements stores in one single row.

#for example

import numpy as np

myArray= np.array(['This','is','single','array']) #note when we use numpy only single data type elements can store like above we store only string and if we store any number with it then giive us error

# numpy directly store the element back to back in array that's why it is faster then list

print(myArray)# only one datatype element is store for performance



#also study the difference between list and numpy in the form of comments

#it also work in List 

myList=['This','is','single','array','using','list'] # in list we can store multiple data type it not matter in list

# list doesn't store elements directly in list. It create pointer for that element. That's the reason it is slower then numpy array 

print(myList)# list is slower then numpy array
# 18 -2- 25
# today we learn how to convert 1 dimension array to 2 dimension array


# for converting 1 dimension to 2 dimension we use 
#           np.newaxis and  np.expand_dims


import numpy as np

# we can make manually 1 dimension array but we pratice but we use .arange (reshape or shape)  to create single array 


myArray=np.arange(6)
print(myArray)  # output    [0 1 2 3 4 5]

# now we can see it is single dimension array now we convert it in 2 dimension array

twoDim_Array=myArray[np.newaxis, :]
print("\nConverted 2d array :     ",twoDim_Array) # ouput      [[0 1 2 3 4 5]]
# in ouput we cna see [[0 1 2 3 4 5]] it show us 2 dimension array. Double square brackets make it 2 dimensional array [[]].

# if you are confuse in that so lets make a multi dimensional array manually.

multiDimArray =np.array([
    [1,2,3,4],
    [5,6,7,8],
    [9,10,11,12]
])   # see this array is called multidimensional array. If we remove the third row 9 to 12 then it become 2d array and you might notice 
# ([
# [1 row]
# [2 row]
# [3 row]
#])

# if we create singel dimension array then we use only [] one time but when we sue it 2 time it is 2d array and when it is above then 2 then we call it multidimensionla array. I hope we all understand.


# now we are going to make 2d array with the  help of .expand_dims

newArray=np.array([1,2,3,4,5,6])# 1d array
print("\nSingle dimension array : " ,newArray)

# now we convert newArray to 2d array with the help of expand_dims

twoDimArr= np.expand_dims(newArray, axis=1) #axis=0 mean rows and axis=1 mean colum.if you uncomment line 48 and comment line 46 then you see the ouptut in only in one row 

#twoDimArr= np.expand_dims(newArray, axis=0) 
print(twoDimArr)

# We study more about it in advance numpy how we can give multiple axis but I feel happy that you learn it by yourself. Go offical documentation and study how we can do that. We study it later 
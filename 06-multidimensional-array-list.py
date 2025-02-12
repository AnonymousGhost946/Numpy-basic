# 6- 2-25

# today our topic is multidimensional array and list
# we also see the difference between them. so please study the comment because in that we see why we use them

# a multi dimensional array or list is an array that contain multiple array in dimension form. If you study C language the you might familiar with it . It's not totally same but almost near with the concept in C.

import numpy as np

myArray=np.array([
    [1,2,3,4,5],
    [6,7,8,9,10],
    [11,12,13,14,15]
    ])# those who are new in python might understand it is array inside array but not. if array exist inside an array then it is called array inside array. and [] after np.arr([]) si the syntax for declaring multidimensional array 

# now we use np.array () and then [] and iside then we descriebe our 3 dimensional array each row is seperated by , 

print(myArray)




# now mulidimensional list 

myList=[
    ['one',2,'three'],
    ['four',5,6],
    [7,'eight',9]
]
# again we can see we use [] and inside that our multidimensional array exist

# notice here we use different dataype elements because  list allow us. It decrease performace but sometime we don't need peroformace the we can use it there

print(myList)


# now if you familiar array inside array or list inside list then you might familiar with how to access them

# first we print numpy array

#remember counting start from 0 not 1
print('Mean second row second element   :',myArray[1][1]) #output 7
#remember counting start from 0 not 1

# now same for list

print('Third row second element:    ',myList[2][1]) # output            eight

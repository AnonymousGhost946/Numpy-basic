# 12 - 2 25
# before this we study about shapes in 03-array-shapes.py file. 

# but in this tutorial we reshape our array 

# .reshape() , ravale() , flatten


import numpy as np

# we sue some our previous learning method 08-creating-special-array.py file

myArray=np.arange(10)
print(myArray) #output  [0 1 2 3 4 5 6 7 8 9]

# with the help of reshape command we can reshape it . In simpel words we can make it a multidimensional array with the deifne dimension and elements. 

# but we should remember a rule that all element of multidimensional array should be same in lenght 

newArray=myArray.reshape(5,2) #(5,2) mean 5 dimension and 2 elements each dimension have
print(newArray)  

#output    
#  [[0 1]
#  [2 3]
#  [4 5]
#  [6 7]
#  [8 9]]
# 5 dimension and 2 element each dimension have

# next we have ravel()
# ravel() simpel convert multidinmensional array in single array 

# in our previous topic we use reshape(). and now we use reshape to convert back it to single array

singleArray=newArray.ravel()
print(singleArray) # output   [0 1 2 3 4 5 6 7 8 9]

# note ravel can give us view or copy to make sure it we make changes newArray and see is it give us copy or view . Let's go

singleArray[0]=100
print(singleArray) # here ouput is here and it should be 100 but see in original array mean newArray is its first element is chagne in 100 or not . We study about view before and if you not know what it is it simply give us a memory reference

print(newArray) # yes it chagne newArray first elelment value with 100 mean it creates a view but my teacher told me that everytime it create view it a bit confusion. I also do my research yes its a bit confusion.but we can fix that confusion by chekcing it that it  create view or copy

# now we have flatten

# flatten and ravel both work same. But the difference is flatten create a copy but there is a bit confusion in ravel it create  view or copy. But we can check it 

# flatten

arr=np.array([
    [1,2,3,4,5],[6,7,8,9,10]
])

flatenArray=arr.flatten()
print(flatenArray) # output      [ 1  2  3  4  5  6  7  8  9 10]


# now we change the first element value of flattenArray and see it make changes in original array or not if not then it make copy not view

flatenArray[0]=2000

print(flatenArray) #output [2000    2    3    4    5    6    7    8    9   10]

# now if these changes not occur in original mean it create copy not view
print(f"original array below:\n {arr}") # it create copy because it not create any changes in original array


# 23 -2 2025

# In this tutorial we learn about some very basic math built in features 

# np.sum , np. prod

import numpy as np

myArray=np.array([2,4,6,8])

#first we have sum 
sumArray=np.sum(myArray)
print(sumArray) # output 20

# next we have product . Simply multiply all elements together

prodArray=np.prod(myArray)
print(prodArray) # ouput 384
# we can confirm the product
print(2*4*6*8)

# next we have cumulaive sum
# np.cumsum give us the sum at each step

cumArray=np.cumsum(myArray)
print(cumArray) # output [2 6 12 20]
# mean first 2 and 2+4= 6 , 6+6 =12, 12+8 =20 like this.

# next we have cumulative product

cumPrdArray=np.cumprod(myArray)
print(cumPrdArray) # ouput [ 2 8 48 384]  same like sum

# next we have to square root . First we cahnge our value then we apply this

myarr=np.array([4,9,16,25])
squareArray=np.sqrt(myarr)
print(squareArray) #output [2. 3. 4 .5]
# if we take root of these values like 2 power 2 or 2 *2 =4 , 3*3=9 , 4*4=16, 5*5=25

#next we have absoulte values 
# in simple remove negative sign

myArray2=np.array([-4,43,-23])
absArray=np.abs(myArray2)
print(absArray) # output [4 43 23]

# there are more but i think we cover essential as a beginner

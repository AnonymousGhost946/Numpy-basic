# 9-2-25

# in this tutorial we are going to learn some keyword that create a special type of array 

# np.zeros(), np.empty(), np.ones(), np.arrange, np.linspace()

import numpy as np

# np.zeros() this will create a array with all element 0 
myArray = np.zeros(3) #if you not  the ouput come [0. 0. 0.] when we credate array with .zeros it basically use float values same in the case of .one() 
print(myArray)



# next we have np.ones(). It create array with all element 1 and also take the length of the elements

myArray2 = np.ones(11)
print(myArray2)


#next we have np.empty()

myArray3 = np.empty(4)
print(myArray3)


# Note :  if you notice the output then you see it not use , to seperate it with space. But if we want it seperate each element with comman, then we can use .tolist 
print(myArray3.tolist())


# next we have np.arange. From its name you might think that it arrange our element but it create element with the range that we defne in parameter 

myArray4=np.arange(15)
print(myArray4.tolist()) # each element is seperated by comma


# next we have np.linspace

#np.linspace(start, stop, num=50, endpoint=True, retstep=False, dtype=None, axis=0)

# we only take only 3 one start stop and num
# start mean where to start and stop mean how much you have to go and then num mena total length of the elements

# Your taks is go and check what is dtype and asis  what they do 
myArray5=np.linspace(1,20 , num=30) 
print(myArray5)


# nex twe have dtype
# as we study earlier the default data type is float. but we can tell it which data type element we want 

myArray6=np.zeros(4, dtype=np.int64) # int stand for integer  and 64 mean 64 bit
print(myArray6) # all values are integer format not float 

# date 5-2-2025


import numpy as np

#one array should must have one data type elements if we assing different datatype then it show us error. Like below we have only one data type only string array.
myarr=np.array(['one','two','three'])
print(myarr)


# now open 02-list-slice.py now we are going to perform the same task using numpy and see the difference

#in list sliceArr create a new copy but in numpy it create a memory reference
sliceArr=myarr[:2]
print(sliceArr)
print(f'original Array : {myarr}')


#now we are going to change sliceArr and see it modify orginal array or not 

sliceArr[0]='Ten'
print(sliceArr)
print(f"Original array also modify : {myarr}")

# so it clear that in numpy array if we assing a new variabel havind elements of original array then it not make a copy it make a memory reference


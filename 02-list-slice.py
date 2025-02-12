# date   5-2-25

# here we are creating a list 
myarr=[1,2,3,4,5,6,]
print(myarr)

# now we make a new variabel and make is equal to myarr but describel elements

# remember it create a new copy of list with define elements

sliceArr=myarr[1:3] # start include end not include
print(sliceArr)

#now here we make sure that it really make a copy of list or not

#as we can see that we assing 0 value to one and then print both sliceArra and myarr and in the  ouputt we can see that sliceArr doesn't modify original array 
sliceArr[0]='one'

print(sliceArr) #output =   ['one',4]

print(myarr)    #output =   [1,2,3,4,5,6]


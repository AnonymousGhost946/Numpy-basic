# date 5-2-25

# in the previous lesson we learn that slice in numpy creates a view of orginal array. Mean memory reference

# in this lesson we discuss about some array character rules.

import numpy as np

myarr=np.array(['one','two'])

#now we are going to replace (one with this is first element)

myarr[0]='This is first element'
print(myarr)  #output : ['Thi' 'two]

#when we print myarr only 'Thi' is show yep this is known as the dtype='<U4'. In simple words this is element character length rule. Mean that before assigning th new value the (0 element) have 3 character that's th reasong only (Thi) print on the screen

#but in some cases maybe our require element character length is larger then the previous one . 

# To avoid this behavious we use datatype object dtype='object'

newArr=np.array(['one','two','three'], dtype='object')
newArr[0]='This is first Element'
print(newArr)# output ['This is first Element' 'two' 'three']

# Task
# Now our task is to do a little research and find solution how to fix this begaviour except  dtype='object'. like dtype='str' or else

#16 - 2 - 25
 
# today we have a small task related with our learning

# task : 

# Create a 3x3 NumPy array with values ranging from 1 to 9. Then:
#Extract the second row using slicing.
#Flatten the array and find the sum of all elements.
#Reshape the flattened array into a (3, 3) shape again.
#Change the data type of the array to float.

import numpy as np

# our first task is to create 3 dimension array in and each array have 3 elements and their data type is integer

myArray= np.array([
    [1,2,3],
    [4,5,6],
    [7,8,9]
])
print(f"Original array is \n{myArray}\n")

# our next task is extract second array using slicing

sliceArray=myArray[1][0:]
print(f"slice array is : {sliceArray}\n")


# our next task is to flatten the original array mean  myArray not sliceArray ok. If you forget about flatten then move 09-reshape.py file and see what flatten do. I also work on it after 4 days i also visit that file and confirm what flatten do. I am not robot i am human and i am happy with forgetting things every pro doesn't remember all the attribute and code etc.

print("\nNow we are pinting flatten array\n")
flatenArray=myArray.flatten()
print(f"Flatten array is : \t {flatenArray}\n")



# out next step is to sum all the elements of the flatenArray

total_sum=np.sum(flatenArray)
print(f"Total sum is :\t {total_sum}\n")

#our last step is to change its data type total_sum  in float

floatArray=np.array(total_sum , dtype='float')
print(f"Array in float data type :\t{floatArray}\n")





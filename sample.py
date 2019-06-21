import numpy as np

# create a list
my_list1 = [1, 2, 3]
my_list2 = [2, 5, 7]
my_list3 = [4, 6, 8]

# create an array using this list
# my_array = np.array(my_list1)
my_array = np.array([my_list1, my_list2, my_list3])


# usage of shape
print(my_array.shape)


# finding out the datatype of the members of the array
print(my_array.dtype)

# zeros, ones, range, empty,

new_array1 = np.zeros([5, 5])  # creates a new numpy array of size 5 with 0 elems


new_array2 = np.empty([5, 5])

new_array3 = np.ones([5, 5])
# identity matrix
new_array4 = np.eye(5)
print(new_array4)

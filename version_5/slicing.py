x = ['a','b','c','d','e','f','g','h','i','j']  #list of characters
print("Original List:", x)
print('---------------------------------------------------------------')

#slicing from index 2 to 5 (5 not included)
sliced_x = x[2:5]
print("Sliced List (index 2 to 5):", sliced_x)
print('---------------------------------------------------------------')


z = x[:4]  #slicing from start to index 4 (4 not included)
print("Sliced List (start to index 4):", z)
print('---------------------------------------------------------------')

e = x[:-1]  #slicing from start to  last element
print("Sliced List (start to second last element):", e)
print('---------------------------------------------------------------')

n = x[0:-1] #slicing from index 0 to last element.  (we can get all elements except last element)
print("Sliced List (index 0 to second last element):", n)



#we can get value in array 
print('---------------------------------------------------------------')
r = x [1:4] #slicing from index 1 to 4 (4 not included)
print("Sliced List (index 1 to 4):", r)
print('---------------------------------------------------------------')


print(len(x))  #length of the list
print('---------------------------------------------------------------')

d = x[1:-1]  #slicing from index 1 to second last element
print("Sliced List (index 1 to second last element):", d)
print('---------------------------------------------------------------')
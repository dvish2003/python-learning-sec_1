x = [22,21,34,23,12,45] #list of integers
y = ["apple", "banana", "cherry"] #list of strings

z = x + y #concatenating two lists
print("Concatenated List:", z)

print("Original List:", x)

y = x[0] #assigning first element of list to variable y
print("First Element:", y)


x.append(56) #adding new element at index 6
print("List after appending 56:", x)

x.insert(2, 67) #inserting 67 at index 2
print("List after inserting 67 at index 2:", x)

x.remove(23) #removing element 23 from the list
print("List after removing 23:", x)

x.pop(0) #removing element at index 0
print("List after popping element at index 0:", x)

x.sort() #sorting the list in ascending order
print("Sorted List:", x)

is_21_in_list_x = 21 in x #checking if 21 is in the list
print("Is 21 in list x?:", is_21_in_list_x)

is_100_in_list_x = 100 not in x #checking if 100 is not in the list
print("Is 100 not in list x?:", is_100_in_list_x)
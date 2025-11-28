x = [12,23,43,45,123,56,78,90]

# Using a for loop with an external index variable
index = 0
# Iterate through each item in the list
# we can get index and value use that use that step it solution 1
for item in x:
    y = x[index]
    print(index, item)
    index += 1


#we can get index and value use that use that step it solution 2
for item in enumerate(x):
    index = item[0]
    value = item[1]
    print(index, value)
    print(type(item), item)
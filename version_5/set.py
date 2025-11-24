x = {'hello', 'hi', 'hey', 'hello'}  # set will automatically remove duplicate values
print(x)  # Output: {'hello', 'hi', 'hey'}
print('---------------------------------------------------------------')

x.add('greetings')  # adding new element to set
print(x)
print('---------------------------------------------------------------')
x.remove('hi')  # removing element from set
print(x)
print('---------------------------------------------------------------')
for item in x:  # iterating through set elements
    print(item)
print('---------------------------------------------------------------')
y = x.copy()  # creating a copy of the set
y.add('welcome')  # modifying the copy
print("Original set:", x)
print("Modified copy:", y)


print('---------------------------------------------------------------')
z = {'12', 45, 78, 12, 45}  # another set with duplicate values
e = {'12',14,'hello',78.5}

n = z.union(e)  # union of two sets
print("Union of sets z and e:", n)
print('---------------------------------------------------------------')

#use pipe
n = z | e  # union using pipe operator
print("Union of sets z and e using pipe operator:", n)
print('---------------------------------------------------------------')

i = z-e  # difference of two sets
print("Difference of sets z and e (z - e):", i)
print('---------------------------------------------------------------')

#find element
is_78_in_z = 78 in z  # checking if 78 is in set z
print("Is 78 in set z?:", is_78_in_z)
print('---------------------------------------------------------------')
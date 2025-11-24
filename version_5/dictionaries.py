x = {'1000':'Alice', '1001':'Bob', '1002':'Charlie'} #dictionary with string keys and values
y = {1:'Math', 2:'Science', 3:'History'} #dictionary with integer keys and string values

print('---------------------------------------------------------------')
x[1250] = 'David' #adding new key-value pair to dictionary x
print("Dictionary x after adding new key-value pair:", x)
 
print('---------------------------------------------------------------')

x['country'] = 'USA' #adding new key-value pair with variable key
print("Dictionary x after adding 'country':", x)

print('---------------------------------------------------------------')

x['city'] = {1:'new york' , 2:'los angeles'} #adding new key-value pair with string key
print("Dictionary x after adding 'city':", x)

print('---------------------------------------------------------------')


print(x.keys()) #printing all keys in dictionary x
print(x.values()) #printing all values in dictionary x


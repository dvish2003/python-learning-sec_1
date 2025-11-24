x = {
    'a':['hello', 'hi', 'hey'],
    'b':['apple', 'banana', 'cherry'],
    'c':['red', 'blue', 'green'],
    'f':15
}

y = x['a']  #if we want to access the list associated with key 'a'. that is not a copy its same element value if change y  its affect x  'a' keyvalue value
print("List associated with key 'a':", y)

z = x['f']   #accessing second element of list associated with key 'b'
z = 90  #changing the value of z does not affect x
print('---------------------------------------------------------------')
y.append('greetings')
print('---------------------------------------------------------------')
print(y)
print('---------------------------------------------------------------')
print(x)
print('---------------------------------------------------------------')
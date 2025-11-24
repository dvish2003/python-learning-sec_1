#tuple is a collection which is ordered and unchangeable. Allows duplicate members.

vishan = ('vishan','vishan', 21, 'Sri Lanka', 'IJSE' )  

name = vishan[0]  #accessing first element of tuple
age = vishan[1]   #accessing second element of tuple
print("Name:", name)
print("Age:", age)

print(vishan.count('vishan'))  #counting occurrences of 'vishan' in tuple

print('---------------------------------------------------------------')

x = (1,'vishan',55)
print(type(x))  #checking the type of x

index,name,weight = x  #unpacking tuple into variables
print("Index:", index)
print("Name:", name)
print("Weight:", weight)

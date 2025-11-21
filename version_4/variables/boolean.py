age = 18
age2 = 20

is_adult = age >= 18
is_minor = age < 18
print("Is adult:", is_adult)
print("Is minor:", is_minor)

print("--------------------------------------------------------------")
#comparing boolean values
is_student = True
is_employed = False
 
is_Student = age == 18
is_Employed = age2 != 20
print("Is student:", is_Student)
print("Is employed:", is_Employed)
print("--------------------------------------------------------------")

#logical operations
a = True
b = False

c = a and b
d = a or b
e = not a
f = not b
g = a ^ b  # XOR operation
print("a and b:", c)
print("a or b:", d)
print("not a:", e)
print("not b:", f)  
print("a ^ b (XOR):", g) #if both are different return true else false
print("--------------------------------------------------------------")

#identity operations
x = 5
y = 5
z = 10



print("Enter your marks:", end=' ')
marks = input()
result = ""

if int(marks) < 0 or int(marks) > 100:
    result = 'Invalid Input'
elif int(marks) >= 0 and int(marks) <= 35:
    result = 'W'
elif int(marks) > 35 and int(marks) <= 50:
    result = 'D'
elif int(marks) > 50 and int(marks) <= 60:
    result = 'C'
elif int(marks) > 60 and int(marks) <= 80:
    result = 'B'
elif int(marks) > 80 and int(marks) <= 100:
    result = 'A'


print("Your grade is:", result)
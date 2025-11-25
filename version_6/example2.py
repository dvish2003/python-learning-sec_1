print("Enter your height in cm: ",end ='')
height = input()


#if int(height) >= 150:
#    job = 'Security Guard'
#else:
#    job = 'Usher'
#
#print("Your job role is:", job)



#  above code is long

job = 'Security Guard' if int(height) >= 150 else 'Usher'
print("Your job role is:", job)


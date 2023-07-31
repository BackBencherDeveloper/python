# Question:
# Take an input from the user and on the basis of that input print the triangular pattern.
# input:
# 3
# output:
# 1
# 12
# 123
# input:
# 4
# Output:
# 1
# 12
# 123
# 1234

#Solution:

a=int(input()) #taking input form the user
b=1 #created a storage for outer loop
while b<=a: #Outer loop will run until b becomes equal to a
    c=1 #Created storage for the inner loop
    while c<=b: #inner loop will run until c become equal to b
        print(c,end="") #printing c everytime as c starts from 1 everytime and keep incrementing by 1
        c+=1 #incrementing c by 1
    b+=1 #incrementing b by 1
    print() #used to change the row once the row is completed
print()
#Question 2: Use that same input to make the below pattern:
# 1
# 23
# 345
# 4567
#Solution:

b=1 #created a storage for outer loop
while b<=a: #Outer loop will run until b becomes equal to a
    c=1 #Created storage for the inner loop
    while c<=b: #inner loop will run until c become equal to b
        print(b+c-1,end="") #printing b+c-1 everytime to get the desired output
        c+=1 #incrementing c by 1
    b+=1 #incrementing b by 1
    print() #used to change the row once the row is completed
print()
#Question3:
#Using the same input print the following pattern:
# input:4
# output:
# 1
# 23
# 456
# 78910
#Solution:

b=1 #created a storage for outer loop
d=1
while b<=a: #Outer loop will run until b becomes equal to a
    c=1 #Created storage for the inner loop
    while c<=b: #inner loop will run until c become equal to b
        print(d,end="") #printing d everytime to get the desired output
        d+=1
        c+=1 #incrementing c by 1
    b+=1 #incrementing b by 1
    print() #used to change the row once the row is complete
    
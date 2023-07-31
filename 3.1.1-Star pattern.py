# #Writing our first code for star pattern.
# Question :
# You need to take an integer input from the user and make a star pattern as per user input.
# input:
# 4
# output:
# ****
# ****
# ****
# ****
# input:
# 3
# output:
# ***
# ***
# ***

# Solution:

#Taking input from the User:
n=int(input()) #Taking input from the user
a=1 #stored 1 in a, we will use this in while loop
while a<=n: #this loop wll continue repeat itself n times
    b=1 #stored 1 in b, we will use this in second while loop.
    while b<=n: #this loop wll continue repeat itself n times
        print("*",end="") #We will print * using this loop ,(here we used end="" to print star's in same line)
        b+=1 #incrementing b to prevent from infinite loop
    print() #using print statement to change the row after the above while loop breaks
    a+=1 #incrementing a to prevent from the infinite loop 

# Now update the above solution so that we get the output like this:
# input:
# 4
# Output:
# * * * *
# * * * *
# * * * *
# * * * *

# Solution
# will not explain everything as code is similar to the above solution:
#Taking input from the User:
#Method 1:
n=int(input()) 
a=1 
while a<=n: 
    b=1
    while b<=n: 
        print("*",end="") 
        print(" ",end="") #we added this to print a space between every star in a row
        b+=1 
    print() 
    a+=1 
#Method 2:
n=int(input()) 
a=1 
while a<=n: 
    b=1
    while b<=n: 
        print("*",end=" ") #so we can add space in end statement soo that this will add an space after every star.
        b+=1 
    print() 
    a+=1 
# Question:
# Sum of Even Numbers
# Send Feedback
# Given a number N, print sum of all even numbers from 1 to N.
# Input Format :
# Integer N
# Output Format :
# Required Sum 
# Sample Input 1 :
#  6
# Sample Output 1 :
# 12

#Solution:

#Taking input:
n=int(input())#taking input form the user 
a=0 #a initialy is 0
c=0 #use to store the sum of the even numbers
#Now there are two methods of doing this using if statement and the second is without if statement:
#Method 1: Using if statement
while a<=n: #first condition of 
    if a%2==0:
        c=c+a
    a+=1
print (c," by method 1")
a=0 #for second method changing a to 0 because of above while loop a is now equal to user input
c=0 #as c store the sum we need to change c also
#Method 2: Without using if statement:
while a<=n:
    c=c+a
    a+=2
print (c," by method 2")



        
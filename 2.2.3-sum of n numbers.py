# Question:
# Sum of n numbers
# Send Feedback
# Given an integer n, find and print the sum of numbers from 1 to n.
# Note
# Use while loop only.
# Input Format :
# Integer n
# Output Format :
# Sum of numbers
# Constraints :
# 1 <= n <= 100
# Sample Input :
# 10
# Sample Output :
# 55

#Solution:
#Till now we know about while loop and we know how to print 1 to n (user input).
# Now we have to change a little bit of code to get the desired output:

#taking input:
n=int(input()) #user will give the input.
a=1 #we will start from 1 and increment this till the user's input one by one.
c=0 #initially it is 0 but we need to print the sum of n numbers so we will store the sum in this
#applying the while loop below:
while a<=n:#applied condition to reach till n
    c=c+a #storing sum of the numbers till n
    a+=1 #incrementing a by one every time to go till n.
print(c) #printing c as it store the sum of n numbers.


# Question
# Check number
# Given an integer n, find if n is positive, negative or 0.
# If n is positive, print "Positive"
# If n is negative, print "Negative"
# And if n is equal to 0, print "Zero".
# Input Format :
# Integer n
# Output Format :
# "Positive" or "Negative" or "Zero" (without double quotes)
# Constraints :
# -100 <= n <= 100
# Sample Input 1 :
# 10
# Sample Output 1 :
# Positive
# Sample Input 2 :
# -10
# Sample Output 2 :
# Negative

#Solution"

#Taking input
n=int(input())
# so as per the question we have to check wether: 
# n is positive meanss (greater than 0) 
# or negative means (less than 0)
# or it is equal to 0 
if n>0: #checking is n is greater than 0.
    print("Positive")#if it is greater than 0 this will be executed.
elif n<0: #checking is n is less than 0
    print("Negative")#if it is less than 0 then this wll be executed.
else:#if both the above conditon not met or not executed that means n is 0 then this will be executed.
    print("Zero")#this will be prined if n is equal to 0.
    


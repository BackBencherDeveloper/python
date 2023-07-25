# Nth Fibonacci Number
# The n-th term of Fibonacci series F(n), 
# where F(n) is a function, 
# is calculated using the following formula -
#     F(n) = F(n - 1) + F(n - 2), 
#     Where, F(1) = 1, F(2) = 1


# Provided 'n' you have to find out the n-th Fibonacci Number.
# Handle edges cases like when 'n' = 1 or 'n' = 2 by using conditionals like 
# if else and return what's expected.


# Example :
# Input: 6

# Output: 8

# Explanation: The number is ‘6’ so we have to find the “6th” Fibonacci number.
# So by using the given formula of the Fibonacci series, we get the series:    
# [ 1, 1, 2, 3, 5, 8, 13, 21]
# So the “6th” element is “8” hence we get the output.
# Input Format :
# The first line contains an integer ‘n’.


# Output Format :
# Print the n-th Fibonacci number.
# Sample Input 1:
# 6


# Sample Output 1:
# 8


# Explanation of sample input 1 :
# The number is ‘6’ so we have to find the “6th” Fibonacci number.
# So by using the given formula of the Fibonacci series, we get the series:    
# [ 1, 1, 2, 3, 5, 8, 13, 21]
# So the “6th” element is “8” hence we get the output.


# Expected time complexity :
# The expected time complexity is O(n).


# Constraints:
# 1 <= 'n' <= 10000     
# Where ‘n’ represents the number for which we have to find its equivalent Fibonacci number.

# Time Limit: 1 second

#Solution:
#importing files we need
from os import *
from sys import *
from collections import *
from math import *
#Taking input
n=int(input()) #taking input for finding the nth term
f0=1 #base case 1 for the fibonacci series (1,1,2,3,5) so we stored 1 in base case 1 for 1st term
f1=1 #base case 2 for the fibonacci series (1,1,2,3,5) so we stored 1 in base case 1 for 2nd term
#as our first and second term's are created we will start creating series from third term till nth term."
a=3 #to start the loop from third term we stored 3 in a
if n==1 or n==2: #if n is 1 or 2 we will give f0 term as both the places store the same number
    print(f0) #here we print f0 as per if case
else:#otherwise we will calculate the number below
    while a<=n: #initiated while loop till n
        c=f0+f1 #stored sum of f0 and f1 in c
        f0=f1 #updated f0 
        f1=c #updated f1
        a+=1 #incrementing c
    print(c) #printing c it's the value of nth term in fibonacci series.
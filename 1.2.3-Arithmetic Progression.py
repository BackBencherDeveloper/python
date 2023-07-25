#Question 3
# Arithmetic Progression
# Send Feedback
# You are given first three entries of an arithmetic progression.  
# You have to calculate the common difference and print it.
# Input format:
# The first line of input contains an integer a (1 <= a <= 100)
# The second line of input contains an integer b (1 <= b <= 100) 
# The third line of input contains an integer c (1 <= c <= 100) 
# Constraints:
# Time Limit: 1 second
# Output format:
# The first and only line of output contains the result.  
# Sample Input:
# 1
# 3
# 5
# Sample Output:
# 2

#Solution:

#Arithematic progression is a sequence of number which increase or decrease with the same difference.
#so we need to check the common difference.
a=int(input("enter first number: "))
b=int(input("enter second number: "))
c=int(input("enter third number: "))
d=c-b
e=b-a
if d==e:
    print("common difference between this series is: ",e)
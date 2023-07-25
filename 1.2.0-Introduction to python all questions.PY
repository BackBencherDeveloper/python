#QUESTION: 
#Find average Marks
# Write a program to input marks of three tests of a student (all integers).    
#Then calculate and print the average of all test marks.
# Input format :
# 3 Test marks (in different lines)
# Output format :
# Average 
# Sample Input 1 :
# 3 
# 4 
# 6
# Sample Output 1 :
# 4.333333333333333
# Sample Input 2 :
# 5 
# 10 
# 5
# Sample Output 2 :
# 6.666666666666667

#SOLUTION:
a=int(input("input first test marks: "))
b=int(input("input first test marks: "))
c=int(input("input first test marks: "))
print((a+b+c)/3)
print()

#QUESTION 2:
#Find X raised to power N
#You are given two numbers ’x’(it’s a float), and ’n’(it’s a integer).
#Your task is to calculate ‘x’ raised to power ‘n’, and return it.
#The expected time complexity is ’O(logn)’, and the expected space complexity is ’O(1)’, 
# where ‘n’ is the power to which the number should be raised.
#Note:
#In the output, you will see the number returned by you upto 6 decimal places.
#Example:
#Input: ‘x’ = 10, ‘n’ = 4
#Output: 10000.000000
#Explanation: On raising ‘x’ to the power of ‘n’, the result is 10000.
#Input Format
#The first line contains two numbers, ‘x’, and ‘n’, denoting the number to be raised 
#and the power to which it should be raised.
#Output format:
#Return the number as described above.
#Sample Input 1:
#10 4
#Sample Output 1 :
#10000.000000
#Explanation Of Sample Input 1:
#Input: ‘x’ = 10, ‘n’ = 4
#Output: 10000.000000
#Explanation: On raising ‘x’ to the power of ‘n’, the result is 10000.
#Sample Input 2:
#3.7 3
#Sample Output 2:
#50.653000
#Explanation Of Sample Input 2:
#Input: ‘x’ = 3.7, ‘n’ = 3
#Output: 50.653000
#Explanation: On raising ‘x’ to the power of ‘n’, the result is 50.653.
#Constraints:
#-9 <= n <= 9
#1 <= x <= 50
#Time Limit: 1-sec

#SOLUTION
x=float(input("input float number: "))
n=int(input("input integer number: "))
a=x**n #here double star is used to get the power of the number so here it means (x*x) n times or 
#x raise to the power of n
print("%6f" % a)#here as per the question we want answer upto 6 decimal digits so we used "%6f",
#and a % before storage. we can also use "{:.6f}".format(a) you can check this below:
print()
print("{:.6f}".format(a)) #this will also give the same result.

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

#Question4: 
# Rectangular Area
# You are given a rectangle in a plane whose sides are parallel to the axes.
# The coordinates of one of its diagonals are provided to you.
# You have to print the total area of the rectangle.
# The coordinates of the rectangle are provided as four integral values: x1, y1, x2, y2. 
# It is given that x1 < x2 and y1 < y2.

# Input format:
# The first line of input contains an integer x1 
# The second line of input contains an integer y1  
# The third line of input contains an integer x2 
# The fourth line of input contains an integer y2 
# Constraints:
# 1 <= x1 <= 10
# 1 <= y1 <= 10
# 1 <= x2 <= 10
# 1 <= y2 <= 10 
# Time Limit: 1 second
# Output format:
# The first and only line of output contains the result.  
# Sample Input:
# 1
# 1
# 3
# 3
# Sample Output:
# 4
# Explanation:
# The given coordinates of the diagonal are (x1,y1) = (1,1) and (x2,y2) = (3, 3). 
# The area of the rectangle can then easily be calculated as: 
# (3 – 1) * ( 3 – 1) = 2 * 2 = 4 

#Solution:

x1=float(input())
y1=float(input())
x2=float(input())
y2=float(input())
#now we have two cordinated we need to find first total length and breath of the rectangle.
#total length will be equal to the difference between the coordinates of y axis.
#total breath will be equal to the difference between the cordinates of x axis.
l=y2-y1 #because as per the question the y2 is always greatter than y1.
b=x1-x2 #because as per the question the x2 is always greatter than x1.
#Now we will multiply l and b for the output
c=l*b
#Now we will print the output
print(c)
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
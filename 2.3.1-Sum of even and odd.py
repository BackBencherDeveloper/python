# Question:
# Sum of even & odd
# Write a program to input an integer 'n' and print the sum of all its even digits and 
# sum of all its odd digits separately.
# Digits mean numbers, not the places! That is, if the given integer is "132456", 
# even digits are 2, 4 and 6 and odd digits are 1, 3 and 5.
# Example :
# Input: 'n' = 132456
# Output: 12 9
# Explanation:
# The sum of even digits = 2 + 4 + 6 = 12
# The sum of odd digits = 1 + 3 + 5 = 9
# Input format :
# The first line contains an integer 'n'.
# Output format :
# In a single line, print two space separated integers, first the sum of even digits, 
# and then the sum of odd digits.
# Sample Input 1:
# 132456
# Sample Output 1:
# 12 9
# Explanation of sample input 1 :
# The sum of even digits = 2 + 4 + 6 = 12
# The sum of odd digits = 1 + 3 + 5 = 9
# Sample Input 2:
# 552245
# Sample Output 2:
# 8 15

#Solution:
#Taking input 
n=int(input()) #Taking n as input from the user
b=0 #this storage is created to hold the sum of all even numbers 
c=0 #this storage is created to hold the sum of all the odd number
while n>9: #the loop will run till n is greater than 9
    a=int(n%10) #added the remainder in a
    n=n-a #removed the last digit from n and updated it to n
    n=n//10 #removed the 0 from the last
    if a%2==0: #checking the number is even or odd
        b=b+a #if it is even updating the even sum
    else: #if not even then
        c=c+a #updating the odd value
#once the loop ends
#repeat the same if else statement once for the last value of n
if n%2==0: 
    b=b+n
else:
    c=c+n
print(b) #print even sum 
print(c) #print odd sum
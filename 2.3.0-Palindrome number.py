# Question:
# Palindrome number

# Check whether a given number ’n’ is a palindrome number.
# Palindrome numbers are the numbers that don't change when reversed.
# Return boolean value true or false.
# Note:
# You don’t need to print anything. Just implement the given function.
# Example:
# Input: 'n' = 51415
# Output: true
# Explanation: On reversing, 51415 gives 51415.
# Input Format:
# The first and only line of the input contains the number 'n'.
# Output format:
# Return a boolean value True or False.
# Sample Input 1 :
# 1032
# Sample Output 1 :
# false
# Explanation Of Sample Input 1:
# 1032, on being reversed, gives 2301, which is a totally different number.
# Sample Input 2 :
# 121
# Sample Output 2 :
# true
# Explanation Of Sample Input 2:
# 121, on being reversed, gives 121, which is the same.
# Expected time complexity:
# The expected time complexity is O(log(n)).
# Constraints :
# 1 <= n <= 10^9
# Time Limit: 1 sec

# Solution:
# Taking input
n=int(input())
# Now there are two methods of doing this 1:Mathematical method 2:Using String

# Method 1:
b=n #Stored n in b
c=0 #taken a new storage c =0
while b>9: #used the loop until b is greater than 9
    d=b%10 #stored the remainder of b/10(divide by 10 to find the last number) in d 
    c=(c*10)+d #updated the value of c by adding d in it (multiply c by 10 for correct position update)
    d=0 #Changed the value of c back to 0
    b=b//10 #divided b to remove the last value which is already added in c
#after the loop condition:
c=(c*10)+b #added the last value in c from b at its correct position.
if c==n: #checked that c==n if yes then the number is palindrome
    print(True) #print true if it is a palindrome 
else: #else condition don't need anything
    print(False) #print false if it is not a palindrome

#method 2:
b=n #Stored n in b
c=0 #taken a new storage c =0
c=str(c)#changed the type of c from integer to string
while b>9: #used the loop until b is greater than 9
    d=b%10 #stored the remainder of b/10(divide by 10 to find the last number) in d
    d=str(d) #changed the type of d from integer to string
    c=c+d #conatinated d to c and updated the value of c.
    d=int(0) #changed the type of d from string to integer
    b=b//10 #divided b to remove the last value which is already added in c
#after the loop condition:
c=c+str(b) #changed the type of b to string from integer and concatinated the value of b in c and updated c
c=int(c) #Changed the type of c from  string to integer
if c==n: #checked that c==n if yes then the number is palindrome
    print(True) #print true if it is a palindrome 
else: #else condition don't need anything
    print(False) #print false if it is not a palindrome
# Code : Square Pattern
# Print the following pattern for the given N number of rows.
# Pattern for N = 4
# 4444
# 4444
# 4444
# 4444
# Input format :
# Integer N (Total no. of rows)
# Output format :
# Pattern in N lines
# Constraints
# 0 <= N <= 50
# Sample Input 1:
# 7
# Sample Output 1:
# 7777777
# 7777777
# 7777777
# 7777777
# 7777777
# 7777777
# 7777777
# Sample Input 1:
# 6
# Sample Output 1:
# 666666
# 666666
# 666666
# 666666
# 666666
# 666666

#Solution:

#Taking input
n=int(input())
a=0 #stored o in a.
while a<n: #using loop to run the code n times
    b=0 #stored 0 in b
    while b<n: #using loop to run the code n times
        print(n,end="") #this will print a row of n, n times.
        b+=1 #increasing b to prevent from the infinite looping.
    print() #this will change the row.
    a+=1 #increasing a to prevent from the infinite looping.

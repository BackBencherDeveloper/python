# Question:
# Reverse of a number
# Write a program to generate the reverse of a given number N. Print the corresponding reverse number.
# Note : If a number has trailing zeros, then its reverse will not include them. 
# For e.g., reverse of 10400 will be 401 instead of 00401.
# Input format :
# Integer N
# Output format :
# Corresponding reverse number
# Constraints:
# 0 <= N < 10^8
# Sample Input 1 :
# 1234
# Sample Output 1 :
# 4321
# Sample Input 2 :
# 1980
# Sample Output 2 :
# 891
#Taking input
N=int(input("Enter your number: ")) #Taking number from the user
b=0 #Created a storage to store a reverse of the user input

#Now there are two methods to perform this task: 1: Mathematical method 2: Using string:

#Method 1:

while N>9: #use the loop while N is greater than 9
    if N%10!=0: #this statement check that the remainder is 0 or not
        a=N%10 #if remainder is not 0 then we store the reminder in a
        N=N//10 #then we do integer divide using double slash (//) of N to remove the last number
        b=(b*10)+a #then we multiply b by 10 everytime and add a(remainder which we get by modulas) 
        a=0 #changed the value of a back to 0. to store new remainder again
    elif N%10==0 and b!=0: #check if remainder is 0 and b is not 0 then follow the below code.
        b=(b*10) #to add the 0(remainder) mutilpy b by 10
        N=N//10 #then we do integer divide using double slash (//) of N to remove the last number
    else: #if the remainder is 0 and b is also 0
        N=N//10 #then we do integer divide using double slash (//) of N to remove the last number
#Now once the loop ends and N is not greater than 9:
b=(b*10)+N #then we one last time multiply b by 10 and add N
print(b) #Finally our number is reversed and we print that.
b=0

# Method 2:
b=str(b) #here we need b in string format so we changed b=0 to b=str(b)
while N>9: #use the loop while N is greater than 9
    if N%10!=0: #this statement check that the remainder is 0 or not
        a=N%10 #if remainder is not 0 then we store the reminder in a
        a=str(a) #then we convert a into string
        N=N//10 #then we do integer divide using double slash (//) of N to remove the last number
        b=b+a #here b and a is integer so we concatinated b and a and again stored in b
        a=int(0) #here we convert a back to integer
    elif N%10==0 and b!=0: #check if remainder is 0 and b is not 0 then follow the below code.
        b=b+'0' #here we add or concatinate 0 in string b 
        N=N//10 #then we do integer divide using double slash (//) of N to remove the last number
    else: #if the remainder is 0 and b is also 0
        N=N//10 #then we do integer divide using double slash (//) of N to remove the last number
#Now once the loop ends and N is not greater than 9:
b=b+str(N) #atlast we changed the last number stored in N to string and concatinated it in b and stored in b.
b=int(b) #here we convert b into integer 
print(b) #then we print b

#the whole process is quite similar... 
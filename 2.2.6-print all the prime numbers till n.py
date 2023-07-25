# Question:
# Given a number n you need to print all the prime number's till n.

#Solution:
#taking input:
n=int(input())
a=2 #we will use this to iterate til (n-1) 
while a<n: #using a to iterate till n-1
    b=2 #we will use this to check that the current number is prime or not.
    flag=False #assigning False value to flag whenever loop initiate again
    while b<a: #using b to iterate till a-1
        if a%b==0 & a!=b: #checking is a is divisible by b or not using modulas
            flag=True #if a is divisible by b then flag will become true and then we will skip line 16.
        b+=1 #incrementing b by 1 everytime
    if flag==False: #Checking the flag value if it is False then we will execute line 16.
        print(a, " is a prime number") #if flag value is False then this will be executed.
    a+=1 #incrementing a by 1.
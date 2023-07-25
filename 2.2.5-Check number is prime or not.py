# #Question:
# Given an integer n you need to check whether n is prime or not if  n is prime print n(number) is prime
# if  n is not prime then print n(number) is no prime.

#Solution:
#step 1: first we will take input
#Taking input:
n=int(input("Enter your number to check prime or not: "))
a=2 #start the number from 2 as prime number is only divisible by 1 or itself. we will use this to divide n.
flag=False #as we did not divided yet n from any number we will initially keep this false.
#flag is just a boolean type data. Nothing else its a normal variable.
#step 2:start the while loop from 2 till n-1 number :
while a<n: #a<n here means we will check from a to n-1 number.
    if n%a==0: #here we will check that the number is divisible by a or not. 
        flag=True #if it is divisible by any number between 2-(n-1) then we will change the flag to true.
    a+=1 #incrementing a by 1 everytime.
#after coming out of loop we will check that the flag is true or false.
if flag==True: #if this condition met or if flag is true then:
    print (n, " is not a prime number") #we will print n(number) is not prime.
else: #otherwise if flag is false then:
    print (n, " is a prime number") #we will print n(number) is a prime.

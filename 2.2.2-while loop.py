# Question:
#what is the requirement of the loops?

#Answer:
#Loops are required to perform bunch of same code multiple times for the desired output.
#this also drecrease the code and and save the time.
#we can run the code till the user want by taking input from the user.

#Question:
#Create a code which prints numbers from 1 to 10 using while loop?

#below is the example of while loop:

#Solution:
a=1
while a<=10: #I used a condition initialy a=1 when a is more than 10 this will break
    print(a) # This will print a till the above condition(a<=10) is true.
    a+=1 # To prevent from infinite looping we increase a with 1 every time.
#once a will become greater than 10 this loop will break.
#We can also print the number from 1 to user's specific number or user input:
#for example:
a=int(input("Enter the number till you want to print: "))
b=1
while b<=a:
    print(b)
    b+=15

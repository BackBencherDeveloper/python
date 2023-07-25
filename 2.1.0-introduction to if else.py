a=True
b=False
# We use if conditon below if is used to check whether the condition is True or False. So:
if a: #it the condition is true then the condition written in if statement will be executed
    #and the statement written in else will be skipped.
    print("I am True because I am a")# this will be executed if the condition is true.
else: #if the condition is not True only then this will be executed 
    #and the statement written in if will be skipped
    print("I am False because I am b")# this will be executed if condition is false 
if not b:
    print("I am False because I am b")
else:
    print("I am True because I am a")
#remember else is not necessary in this if you will not give else then it will print if statement only if:
#the condition is satisfied else if will print nothing .
#for example: we will print{input is even} if the input is even only.
a=int(input())
if a%2==0:
    print("input is even")
#we can also use else if statement if we have more than two options and we have to execute one of them as per
#condition
a=int(input())
b=int(input())
c=int(input())
if a>=b and a>=c:
    print("First input is greater i.e: ", a)
elif b>=a and b>=c:
    print("Second input is greater i.e: ", b)
else:
    print("Third input is greater i.e: ", b)

#Now there is one more thing known as nested if and else statement:
#we can use elif in that also in nested loops and in loops

#we will take n and m from user(both integers) and then:
# we need to check:
# if n is even: then we will check m is even and is not equal to 1:
# if both are even and m is not equal to 1 we will print 1
# if n is even: then we will check m is even and is not equal to 1: 
# if m is even and is equal to 1 we will print 2.
#if n is even and m is not even then we will print 3
#if n is not even then we will print 0.

#for this we need to use even and odd conditions and we need to check it is equal to 1 or not 

#Solution

#taking input
n=int(input())
m=int(input())
#checking conditions:
if n%2==0: #checking  n is even or not if n is even then we will go inside this then:
    if m%2==0 and m!=1: #checking if m is even and is not equal to 1 if this is correct then:
        print(1) #we will print 1 if both m and n are even and m is not equal to 1
    elif m%2==0 and m==1: # checking that m is even and is equal to 1 if this is correct then:
        print(2) # we will print 2 if both m and n are even and m is equal to 1
    else:# if both the above condition are not executed that means m is not even then:
        print(3) #we will print 3 in this case
else: # if n is not even we will execute this:
    print(0) # we will print 0 if n is not even as per the question.

#so this was the example of nested loop in which we used else if in inner loop. 
# Similarly We can use elif in outer loop also as per the question requirments.
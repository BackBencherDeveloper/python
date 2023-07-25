# Question:
# Calculator
# Write a program that performs the tasks of a simple calculator. 
# The program should first take an integer as input and then based on that integer perform 
# the task as given below.
# 1. If the input is 1, then 2 integers are taken from the user and their sum is printed.
# 2. If the input is 2, then 2 integers are taken from the user and their difference
# (1st number - 2nd number) is printed.
# 3. If the input is 3, then 2 integers are taken from the user and their product is printed.
# 4. If the input is 4, then 2 integers are taken from the user and the quotient obtained 
# (on dividing 1st number by 2nd number) is printed.
# 5. If the input is 5, then 2 integers are taken from the user and their remainder
# (1st number mod 2nd number) is printed.
# 6. If the input is 6, then the program exits.
# 7. For any other input, then print "Invalid Operation".
# Note: Each answer in next line.
# Input format:
# Take integers as input, in accordance to the description of the question. 
# Constraints:
# Time Limit: 1 second
# Output format:
# The output lines must be as prescribed in the description of the question.
# Sample Input:
# 3
# 1
# 2
# 4
# 4
# 2
# 1
# 3
# 2
# 7
# 6
# Sample Output:
# 2
# 2
# 5
# Invalid Operation
# Explanation of the sample input
# The first number given is 3, so that means two more numbers will be given and
# we'll have to multiply them and show the result. 
# The two numbers are 1 and 2. Their product is 2, so 2 is displayed first in the output. 
# Similarly, all the numbers are processed in groups of three. 
# The first number tells the operation and the next two numbers tell 
# on which numbers the operation is done. 
# This applies to numbers from 1 to 5. 
# If the input is 6 (like it is at the end), two more numbers will NOT be provided,
# you simply have to exit the program. 
# Also, if the input is any number except 1 to 6 (like 7 which is at the second last),
# then you simply have to print "Invalid Operation"

#Solution:

# as we don't need to end the process till the user enter 6 as an option
while True: #using while loop for keep the process running again and again
    a=int(input()) #taking input from the user 
    if a>=1 and a<=5: # as per question cecking the input is equal to or more than 1 or max 5 
        b=int(input()) #taking input of first value
        c=int(input()) #taking input of second value
        if a==1:    #whole evaluation as per input done from here in inner if and elif's
            a=b+c
        elif a==2:
            a=b-c
        elif a==3:
            a=b*c
        elif a==4:
            a=b/c
        elif a==5:
            a=b%c
        print(a)
    elif a==6: #checking that the user entered 6 or not so than when user enter 6 we will break the operation
        break #used break statement to break the operation
    else: #checking that is user input is different from the above inputs
        print("Invalid Operation") #if yes it is different we will print this.
        
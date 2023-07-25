# Question:
# Fahrenheit to Celsius
# Given three values - Start Fahrenheit Value (S), End Fahrenheit value (E) and Step Size (W),
# you need to convert all Fahrenheit values from Start to End at the gap of W,
# into their corresponding Celsius values and print the table.
# Input Format :
# 3 integers - S, E and W respectively 
# Output Format :
# Fahrenheit to Celsius conversion table. 
# One line for every Fahrenheit and corresponding Celsius value in integer form. 
# The Fahrenheit value and its corresponding Celsius value should be separate by single space.
# Constraints :
# 0 <= S <= 90
# S <= E <=  900
# 0 <= W <= 80 
# Sample Input 1:
# 0 
# 100 
# 20
# Sample Output 1:
# 0   -17
# 20  -6
# 40  4
# 60  15
# 80  26
# 100 37
# Sample Input 2:
# 20
# 119
# 13
# Sample Output 2:
# 20  -6
# 33  0 
# 46  7
# 59  15
# 72  22
# 85  29
# 98  36
# 111 43
# Explanation For Input 2:
# Start calculating the Celsius values 
# for each Fahrenheit Value which starts from 20. So starting from 20,
# we need to compute its corresponding Celsius value which computes to -6.
# We print this information as <Fahrenheit Value> <a single space> <Celsius Value>on each line. 
# Now add 13 to Fahrenheit Value at each step until you reach 119 in this case. 
# You may or may not exactly land on the end value depending on the steps you are taking.

#Solution:
#for this first of all we should know the formula of fahrenheit to celsius coversion:
#Formula:(32°F − 32) × 5/9 = 0°C
#starting F is given
#ending F is given
#gap is given
#Taking input:
sf=int(input("enter starting fahrenheit value: ")) #taking starting fahrenheit value
ef=int(input("enter ending fahrenhiet value: ")) #taking ending fahrenheit value
gap=int(input("enter the gap value: ")) #taking the gap value
while sf<=ef: #loop will continue till sf is less than or equal to ef
    C=int((sf-32)*5/9) #applying the formula of fahrenheit to celsius conversion
    print("Fahrenheit value: ",sf,"  Celsius value: ",C) #printing the values
    sf+=gap #increasing stating fahrenheit value by the gap value

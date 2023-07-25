###PRACTICE OF PYTHON
#print command is used to print anything for example:
print("helloword")
###Variables are used to store the values and inputs for example:
a=input("enter frst number: ")
#in input() what we write in the bracket will be printed to while taking the input
print(a)
b=input("enter second number: ")
c=a+b
print(c)
#answer of a+b=ab in the above case because the default value of the inputs are string
#if we want we can change it to integer using int before input for exmple:
d=int(input("enter third number: "))
#below check the types of a, b, c, and d respectively:
print("type of a is: ",type(a))
print("type of b is: ",type(b))
print("type of c is: ",type(c))
print("type of d is: ",type(d))
#when you run this code you will find the type of a, b, and c is string but,
#the type of d is integer because we defined it as integer
#variables can be uppercase lowercase can be can include numbers and underscore but,
#it cannot start from the any number
#data types:there are different types of data types but as of now we will check only:
#1.INTEGERS
#2.FLOAT
#3.STRING
#4:COMPLEX NUMBERS
#1:INTEGERS:INTEGERS are numerical numbers or a value but not in decimals for ex: 1,5,10.
#2:FLOAT: FLOAT are numerical values contain decimal values for example: 1.5,7.1,2.8 are float
#3:STRING: A combination of some characters are know as STRING for example: "BACKBENCHERS"
#4:COMPLEX NUMBERS are those numbers which include a character in it ex: 1+2j+3l,20j-15l.
e=20+15j
print(type(e))
# in python the variable actually stores the meta data of the value but not store the value of the variable:
#here meta data means the address of that particular value or string or float.
#we can check this with id below is the example:
a=10
b=10
print(id(a))
print(id(b))
#140715695793224 address of a
#140715695793224 address of b
#here both the address are same as both contain the address of 10.
#but if we change the value of one storage to 11 then the address of that storage will change to: address of 11.
#if we assign the same value to a storage between -5 to 256 then address will be same but in jupiter:
#the address will differ and in other interpreter the address will be same
a=1000
b=1000
print(id(a))
print(id(b))
#As in vs code the address remains the same once you will run this in jupiter address will change

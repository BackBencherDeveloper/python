##Boolean are of two types: True or False and to use them as a keyword we don't need double inverted commas
# or single inverted commas. We can use directly: if we use commas then it will become string.
c=True
d=False
print(c)
print(d)
a=10
b=20
print(a>b)
print(b>a)
print()#this will create an empty line between both the above and below answers
#Relational operatio: relational operators are used to find the relation between the variables.
#for example: are they equal,or one of them is greater than or less than the other.
print(a>b)#checks is a is greater than b if yes return True else return False.
print(a<b)#checks is a is less than b if yes return True else return False.
print(a<=b)#checks is a is less than or equal to b if yes return True else return False.
print(a>=b)#checks is a is greater than or equal to b if yes return True else return False.
print(a==b)#checks is a is equal to b if yes return True else return False.
print(a!=b)#checks is a is not equal to b if yes return True else return False.
#logical operators: Logical operators are used to apply logic there are 3 llogical operators: and, or, not
f=a>b and a<=b #On the right and left side of and operator there are conditions.
#If both the conditions are true then f will store True if one of them or both are false then f will store False
print()
print(f)
f= a>b or a<=b #if any one of these conditions or both written on left and right side of or operator is true
#then: f will store True else if both are False then f will store false.
print()
print(f)
f=not a>b #if the condition written in the right side is True then f will not store Ture it will store False
#and if the condition written in the right side is False then f will not store False it will store True 
print(f)
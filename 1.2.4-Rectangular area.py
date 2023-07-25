#Question 4: 
# Rectangular Area
# You are given a rectangle in a plane whose sides are parallel to the axes.
# The coordinates of one of its diagonals are provided to you.
# You have to print the total area of the rectangle.
# The coordinates of the rectangle are provided as four integral values: x1, y1, x2, y2. 
# It is given that x1 < x2 and y1 < y2.

# Input format:
# The first line of input contains an integer x1 
# The second line of input contains an integer y1  
# The third line of input contains an integer x2 
# The fourth line of input contains an integer y2 
# Constraints:
# 1 <= x1 <= 10
# 1 <= y1 <= 10
# 1 <= x2 <= 10
# 1 <= y2 <= 10 
# Time Limit: 1 second
# Output format:
# The first and only line of output contains the result.  
# Sample Input:
# 1
# 1
# 3
# 3
# Sample Output:
# 4
# Explanation:
# The given coordinates of the diagonal are (x1,y1) = (1,1) and (x2,y2) = (3, 3). 
# The area of the rectangle can then easily be calculated as: 
# (3 – 1) * ( 3 – 1) = 2 * 2 = 4 

#Solution:

x1=float(input())
y1=float(input())
x2=float(input())
y2=float(input())
#now we have two cordinated we need to find first total length and breath of the rectangle.
#total length will be equal to the difference between the coordinates of y axis.
#total breath will be equal to the difference between the cordinates of x axis.
l=y2-y1 #because as per the question the y2 is always greatter than y1.
b=x1-x2 #because as per the question the x2 is always greatter than x1.
#Now we will multiply l and b for the output
c=l*b
#Now we will print the output
print(c)
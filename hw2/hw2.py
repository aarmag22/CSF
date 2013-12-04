# Name: Maggie Aaron
# Evergreen Login: aarmag22
# Computer Science Foundations
# Programming as a Way of Life
# Homework 2

# You may do your work by editing this file, or by typing code at the
# command line and copying it into the appropriate part of this file when
# you are done.  When you are done, running this file should compute and
# print the answers to all the problems.

import math
###
### Problem 1      
### Gauss's Problem: Adds natural numbers from 'i' thru 'n' and prints sum.


# DO NOT CHANGE THE FOLLOWING LINE
print "Problem 1 solution follows:"

sum = 0    # running total of values
i = 1      # initial value
n = 100    # final value

while i < n+1:   # use n + 1 to include the final value
    sum = sum + i  
    i = i+1
    
print sum


###
### Problem 2
### Reciprocals: Prints the decimal values of 1 / n

# DO NOT CHANGE THE FOLLOWING LINE
print "Problem 2 solution follows:"

x = 2     # initial value
y = 10    # final value

for i in range (x, y+1):
    r = 1.0/x
    print r
    x = x+1

###
### Problem 3
### Prints the nth Triangular number

# DO NOT CHANGE THE FOLLOWING LINE
print "Problem 3 solution follows:"

n = 10              # final value
triangular = 0      # initial value
for i in range(n+1):
    triangular = triangular + i


print "Triangular number", n, "via loop:", triangular
print "Triangular number", n, "via formula:", (n*(n+1))/2

###
### Problem 4
### Factorial: Prints n!

# DO NOT CHANGE THE FOLLOWING LINE
print "Problem 4 solution follows:"

n = 10
product = 1
for i in range(1,n+1):
    product = product * i
    
print product

###
### Problem 5
### Multiple Factorials

# DO NOT CHANGE THE FOLLOWING LINE
print "Problem 5 solution follows:"

numlines = 10
for j in range(numlines):
    n = numlines-j
    product = 1
    for i in range(1,n+1):
        product = product * i
    print product


###
### Problem 6
### Sum of Reciprocals of Factorials 

# DO NOT CHANGE THE FOLLOWING LINE
print "Problem 6 solution follows:"

numlines = 10
sum = 1
for j in range(numlines):
    n = numlines-j
    product = 1
    for i in range(1,n+1):
        product = product * i
    recip = 1.0/product
    sum = sum + recip
print sum        

###
### Collaboration
###

# Brad Mattix, Khan Academy, interactivepython.org, pythontutor.com 

###
### Reflection
###

# ... Write how long this assignment took you, including doing all the readings
# ... and tutorials linked to from the homework page. Did the readings, tutorials,
# ... and lecture contain everything you needed to complete this assignment?

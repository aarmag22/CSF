# Name: Maggie Aaron, Josh Kendall, Zach Linton
# Evergreen Login: aarmag22, kenjos03, linzac03
# Computer Science Foundations
# Programming as a Way of Life
# Homework 6 Answer Key
# Group 20


# You may do your work by editing this file, or by typing code at the
# command line and copying it into the appropriate part of this file when
# you are done.  When you are done, running this file should compute and
# print the answers to all the problems.


###
### Problem 3
### Assert Statement

# DO NOT CHANGE THE FOLLOWING LINE
print "Problem 3 solution follows:"

a = 2
b = 2

assert a == b

## The assert statement tests the truth value of a program and returns 
## an AssertionError if it is incorrect.

###
### Problem 4
### Defining and Calling Functions

# DO NOT CHANGE THE FOLLOWING LINE
print "Problem 4 solution follows:"

def add(x, y):
    total = x + y
    return total
total = add(a, b)
print total

## Functions are first defined using def, then followed by parentheses, ().

###
### Problem 5
### Creating a Dictionary

# DO NOT CHANGE THE FOLLOWING LINE
print "Problem 5 solution follows:"

v = {"a": 2, "b": 3}

assert v == {"a": 2, "b": 3}

## Dictionaries can be identified by curly braces, {} containing pairs 
## separated by a colon, :.

###
### Problem 6
### Adding Key-Value Pairs to a Dictionary

# DO NOT CHANGE THE FOLLOWING LINE
print "Problem 6 solution follows:"

v2 = {}
v2 ["a"] = 2
v2 ["b"] = 3

assert v == v2

## The method in problem 5 is better suited for a smaller amount of data whereas
## the method in problem 6 can be used when working with larger bodies of data 
## such as what we saw in hw5.

###
### Problem 7
### Utilizing a For Loop and Putting it all Together

# DO NOT CHANGE THE FOLLOWING LINE
print "Problem 7 solution follows:"


for i in v:
    print i
    print v[i]
    
## The first print statement prints the keys, and the second one prints 
## the values associated with the keys.
    

###
### Collaboration
###

# ... List your collaborators and other sources of help here (websites, books, etc.),
# ... as a comment (on a line starting with "#").
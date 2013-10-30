# Name: Maggie Aaron
# Evergreen Login: aarmag22
# Computer Science Foundations
# Programming as a Way of Life
# Homework 1

# You may do your work by editing this file, or by typing code at the
# command line and copying it into the appropriate part of this file when
# you are done.  When you are done, running this file should compute and
# print the answers to all the problems.

import math         # makes the math.sqrt function available


###
### Problem 1
###

print "Problem 1 solution follows:"

a = 1
b = -5.86
c = 8.5408

PlusValue = -b + math.sqrt ((b**2) - (4*a*c))/(2*a)
MinusValue = -b - math.sqrt ((b**2) - (4*a*c))/(2*a)

print PlusValue "&" MinusValue

###
### Problem 2
###

print "Problem 2 solution follows:"

import hw1_test

a = hw1_test.a    #sets variables to corresponding boolean value from hw1_test
b = hw1_test.b
c = hw1_test.c
d = hw1_test.d
e = hw1_test.e
f = hw1_test.f

ListValues = [a, b, c, d, e, f]
for i in ListValues:
  print i  


###
### Problem 3
###

print "Problem 3 solution follows:"

print ((a and b) or (not c) and not (d or e or f))

###
### Collaboration
###

# Brad Mattix

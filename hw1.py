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

y = -b + math.sqrt((b ** 2) - (4 * (a) * (c)))/(2 * (a))
z = -b - math.sqrt((b ** 2) - (4 * (a) * (c)))/(2 * (a))

print y
print z

###
### Problem 2
###

print "Problem 2 solution follows:"

import hw1_test

print hw1_test.a
a = hw1_test.a    #sets a as variable from hw1_test
print hw1_test.b
b = hw1_test.b
print hw1_test.c
c = hw1_test.c
print hw1_test.d
d = hw1_test.d
print hw1_test.e
e = hw1_test.e
print hw1_test.f
f = hw1_test.f

###
### Problem 3
###

print "Problem 3 solution follows:"

print ((a and b) or (not c) and not (d or e or f))

###
### Collaboration
###

# ... List your collaborators here, as a comment (on a line starting with "#").

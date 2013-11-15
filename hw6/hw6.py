# -*- coding: utf-8 -*-
# Name: Maggie Aaron, Josh Kendall, Zach Linton
# Evergreen Login: aarmag22, kenjos03, linzac03
# Computer Science Foundations
# Programming as a Way of Life
# Homework 6
# Group 20


# You may do your work by editing this file, or by typing code at the
# command line and copying it into the appropriate part of this file when
# you are done.  When you are done, running this file should compute and
# print the answers to all the problems.


###
### Problem 3
###

# DO NOT CHANGE THE FOLLOWING LINE
print "Problem 3 solution follows:"

a=1
b=2
c=3

def multi(a,b,c):
    product = a * b * c
    return product

product = multi(a,b,c)

print multi(a,b,c)

###
### Problem 4
###

# DO NOT CHANGE THE FOLLOWING LINE
print "Problem 4 solution follows:"

a = {'a': 1} 
b = {'b': 2} 
c = {'c': 3}

list1 = []
list1.append(a)
list1.append(b)
list1.append(c)

print list1


###
### Problem 5
###

# DO NOT CHANGE THE FOLLOWING LINE
print "Problem 5 solution follows:"

a = [{'Pet': 'Cat', 'Name': 'Bob'}, {'Pet': 'Dog', 'Name':  'Blake'}, {'Pet': 'Bird', 'Name': 'Tweet'}]
for i in a:
    print i

###
### Problem 6
###

# DO NOT CHANGE THE FOLLOWING LINE
print "Problem 6 solution follows:"

a = {'A': 1, 'B': 2,  'C': 3} 
b = {'D': 4,  'E': 5}
c = dict(a.items()+b.items())
print c

###
### Problem 7
###

# DO NOT CHANGE THE FOLLOWING LINE
print "Problem 7 solution follows:"

a = [
{'State': 'WA', 'Bird': 'American Goldfinch', 'Nickname': 'The Evergreen State'}, 
{'State': 'OR', 'Bird': 'Western Meadowlark', 'Nickname': 'Beaver State'},  
{'State': 'CA', 'Bird': 'California Quail', 'Nickname': 'The Golden State'}
]

d = {}
for i in a:
    name = i['State']
    nick = i['Nickname']
    d[name] = nick
print d 

# d[i['State']] = i['Nickname']  Could also do it this way to save space.


###
### Collaboration
###

# ... List your collaborators and other sources of help here (websites, books, etc.),
# ... as a comment (on a line starting with "#").
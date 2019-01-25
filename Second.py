#!/usr/bin/env python

"""[We try to merge two dictionaries to obtain a single. Aim is to reduce run time]
"""


__author__ =  "Ravi Prakash"

# Merging two dictionaries
x = {'v':1, 'i':6, 'l':9}
y = {'s':7, 'h':5, 'a':8, 'l':2}

z = {**x, **y}

print(z)




#!/usr/bin/env python

__author__ =  "Ravi Prakash"

"""Implement function ToLowerCase() that has a string parameter str, and returns the same string in lowercase.

 

Example 1:

Input: "Hello"
Output: "hello"

Returns:
    [str] -- [lower case]
"""

class Solution:
    def toLowerCase(self, str):
        """
        :type str: str
        :rtype: str
        """
        return ''.join(map(lambda x:chr(ord(x)+32) if 90>ord(x)>64 else x, list(str)))

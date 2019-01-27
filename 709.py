#!/usr/bin/env python

__author__ =  "Ravi Prakash"

class Solution:
    def toLowerCase(self, str):
        """
        :type str: str
        :rtype: str
        """
        return ''.join(map(lambda x:chr(ord(x)+32) if 90>ord(x)>64 else x, list(str)))
        
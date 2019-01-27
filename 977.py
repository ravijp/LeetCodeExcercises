#!/usr/bin/env python

__author__ =  "Ravi Prakash"

"""[summary]

Returns:
    [list] -- [Sorted list of squares]
"""



class Solution:
    def sortedSquares(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        return sorted([x*x for x in A])
        
#
# @lc app=leetcode id=149 lang=python3
#
# [149] Max Points on a Line
#

# @lc code=start
from collections import defaultdict
from math import gcd

def get_standard_cononical_form(p1, p2 ):
    #Let p2 be the one with the greatest y
    #in case of time let x coord decide
    if p1[1] > p2[1] or (p1[1] == p2[1] and p1[0] < p2[0]):
        p1, p2 = p2, p1
    A = p2[1] - p1[1]
    B = p1[0] - p2[0]
    C = p2[0]*p1[1] - p1[0]*p2[1]
    div= gcd(A, B, C)
    A //= div
    B //= div
    C //= div
    return A, B, C

class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
    #For each pair of points
    #We check what (infinite) line passes thorugh both points y = ax + b
    #represent that line as a tuple of coefficients, might run into floating point issues
    #I know there exist a representation that only have integer coeffcients, but don't remmeber it off the top
    #use a counter to count how many times a givn tuple occurs
    #It is called the canonical form Ax + By + C = 0
        lineToPoints = defaultdict(set) 
        n = len(points)
        for i in range(n):
            p1 = points[i]
            for j in range(i+1, n):
                p2 = points[j]
                line_tuple = get_standard_cononical_form(p1, p2)
                lineToPoints[line_tuple].add(tuple(p1)) 
                lineToPoints[line_tuple].add(tuple(p2)) 

        maxLen = 1
        for line in lineToPoints:
            maxLen = max(maxLen, len(lineToPoints[line]))

        return maxLen
                
        
# @lc code=end


#
# @lc app=leetcode id=593 lang=python3
#
# [593] Valid Square
#

# @lc code=start
from math import sqrt

def dot(v1, v2):
    return sum(v1[i] * v2[i] for i in range(len(v1)))

def length(vector):
    return sqrt(dot(vector, vector))

def diff(v1, v2):
    return [v1[i] - v2[i] for i in range(len(v1))]


    
    
class Solution:
    def validSquare(self, p1: Tuple[int], p2: Tuple[int], p3: Tuple[int], p4: Tuple[int]) -> bool:
        """   
        we have three vectors, two of them have to the same length(the side of the square).
        the third one will have sqrt(2) side length 
        after sorting the points the walk
        p1, p2, p4, p3, p1 will walk the other perimater of the square
        """
        p1, p2, p3, p4 = sorted([p1, p2, p3, p4])
        v12 = diff(p1, p2)
        v24 = diff(p2, p4)
        v43 = diff(p4, p3)
        v31 = diff(p3, p1)
        side_len2 = dot(v12, v12)
        return (side_len2 > 0 and
                side_len2 == dot(v24, v24) and
                side_len2 == dot(v43, v43) and
                side_len2 == dot(v31, v31) and 
                0 == dot(v12, v31)# make sure that v12 v31 makes a right angle
                )

        
# @lc code=end


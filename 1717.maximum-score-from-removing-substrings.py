#
# @lc app=leetcode id=1717 lang=python3
#
# [1717] Maximum Score From Removing Substrings
#

# @lc code=start

from functools import cache

class Solution:
    def maximumGain(self, s:str, x: int, y:int) -> int:
        #Order the patterns and their points so x and 1 is the one that gives the most points
            
        def remove_pattern(s, pattern, value):
            stack = []
            points = 0
            for c in s:
                if stack and stack[-1] == pattern[0] and c == pattern[1]:
                    stack.pop()
                    points += value
                else:
                    stack.append(c)
            return "".join(stack), points
        
        if x > y:
            pattern1, val1 = "ab", x
            pattern2, val2 = "ba", y
        else:
            pattern1, val1 = "ba", y
            pattern2, val2 = "ab", x
        
        s, points1 = remove_pattern(s, pattern1, val1)
        _, points2 = remove_pattern(s, pattern2, val2)
        return points1 + points2
                    
                    
            
        
class SolutionTLE:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        """DP
        I did not take into account that one option will be preferable for all cases
        which simplifies the problem 
        """


        @cache
        def dp(s, cur_points):
            n = len(s)
            if n < 2:#Both ab and ba contain two chars 
                return cur_points
            
            #print(s, cur_points)
            max_points = cur_points
            for i in range(1, n):
                if s[i-1:i+1] == "ab":
                    max_points = max(dp(s[:i-1] + s[i+1:], cur_points + x ), max_points)
                elif s[i-1:i+1] == "ba":
                    max_points = max(dp(s[:i-1] + s[i+1:], cur_points + y ), max_points)
                
            return max_points
        
        return dp(s, 0)
            
        
# @lc code=end


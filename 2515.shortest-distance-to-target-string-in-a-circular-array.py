#
# @lc app=leetcode id=2515 lang=python3
#
# [2515] Shortest Distance to Target String in a Circular Array
#

# @lc code=start
class Solution:
    def closestTarget(self, words: List[str], target: str, startIndex: int) -> int:
        res = float("inf")

        n = len(words)
        for i, word in enumerate(words):
            if word == target:
                res = min(res, abs(i-startIndex), n - abs(i -startIndex))
        
        return res if res < n else -1
        
# @lc code=end


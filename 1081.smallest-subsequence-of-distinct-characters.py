#
# @lc app=leetcode id=1081 lang=python3
#
# [1081] smallest subsequence of distinct characters
#

# @lc code=start

class Solution:
    def smallestSubsequence(self, s: str) -> str:
        visisted = [0] * 26
        counts = [0] *26

        for char in s:
            counts[ord(char) - ord("a")] += 1
        
        stack    = []

        
        for char in s:
            idx = ord(char) - ord("a")
            counts[idx] -= 1

            if not visisted[idx]:
                while stack and stack[-1] > char:
                    top_idx = ord(stack[-1] ) - ord("a")

                    if counts[top_idx] > 0:
                        visisted[top_idx] = 0
                        stack.pop()
                    else:
                        break
                
                visisted[idx] = 1
                stack.append(char)

        return "".join(stack)
        
# @lc code=end


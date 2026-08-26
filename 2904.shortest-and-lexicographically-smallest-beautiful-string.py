# @lc app=leetcode id=2904 slug=shortest-and-lexicographically-smallest-beautiful-string lang=python3
#
# [2904] Shortest and Lexicographically Smallest Beautiful String
# Difficulty: Medium
# Tags: String, Sliding Window
# URL: https://leetcode.com/problems/shortest-and-lexicographically-smallest-beautiful-string/
#
# @lc code=start
class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        n = len(s)
        cnt = 0 
        result = ""



        l = 0
        for r in range(n):
            if s[r] == "1":
                cnt += 1

            while cnt > k:
                cnt -= s[l] == "1"
                l += 1

            if cnt == k:
                # Remove unnecessary leading zeros
                while s[l] == "0":
                    l += 1

                candidate = s[l:r + 1]

                if (result == "" or
                    len(candidate) < len(result) or
                    (len(candidate) == len(result) and candidate < result)):
                    result = candidate

        return result 




        

# @lc code=end

# @lc app=leetcode id=1520 slug=maximum-number-of-non-overlapping-substrings lang=python3
#
# [1520] Maximum Number of Non-Overlapping Substrings
# Difficulty: Hard
# Tags: Hash Table, String, Greedy, Sorting
# URL: https://leetcode.com/problems/maximum-number-of-non-overlapping-substrings/
#
# @lc code=start
class Solution:
    def maxNumOfSubstrings(self, s: str) -> list[str]:
        first = {}
        last = {}

        for i, c in enumerate(s):
            if c not in first:
                first[c] = i
            last[c] = i

        
        intervals = []

        for c, start in first.items():
            end = last[c]
            i = start
            valid = True

            while i <= end:
                ch = s[i]
                if first[ch] < start:
                    valid = False
                    break
                if last[ch] > end:
                    end = last[ch]
                i += 1
            
            if valid:
                intervals.append((start, end))


        intervals.sort(key= lambda x: x[1])

        res = []
        prev_end = -1

        for start, end in intervals:
            if start > prev_end:
                res.append(s[start:end +1])
                prev_end = end

        return res 
            
        

# @lc code=end

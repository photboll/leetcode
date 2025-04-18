#
# @lc app=leetcode id=38 lang=python3
#
# [38] Count and Say
#
# https://leetcode.com/problems/count-and-say/description/
#
# algorithms
# Medium (58.12%)
# Likes:    4478
# Dislikes: 8683
# Total Accepted:    1.1M
# Total Submissions: 1.9M
# Testcase Example:  '1'
#
# The count-and-say sequence is a sequence of digit strings defined by the
# recursive formula:
# 
# 
# countAndSay(1) = "1"
# countAndSay(n) is the run-length encoding of countAndSay(n - 1).
# 
# 
# Run-length encoding (RLE) is a string compression method that works by
# replacing consecutive identical characters (repeated 2 or more times) with
# the concatenation of the character and the number marking the count of the
# characters (length of the run). For example, to compress the string "3322251"
# we replace "33" with "23", replace "222" with "32", replace "5" with "15" and
# replace "1" with "11". Thus the compressed string becomes "23321511".
# 
# Given a positive integer n, return the n^th element of the count-and-say
# sequence.
# 
# 
# Example 1:
# 
# 
# Input: n = 4
# 
# Output: "1211"
# 
# Explanation:
# 
# 
# countAndSay(1) = "1"
# countAndSay(2) = RLE of "1" = "11"
# countAndSay(3) = RLE of "11" = "21"
# countAndSay(4) = RLE of "21" = "1211"
# 
# 
# 
# Example 2:
# 
# 
# Input: n = 1
# 
# Output: "1"
# 
# Explanation:
# 
# This is the base case.
# 
# 
# 
# Constraints:
# 
# 
# 1 <= n <= 30
# 
# 
# 
# Follow up: Could you solve it iteratively?
#

# @lc code=start
def run_length_encode(s:str):
    encoded = []
    curr_count = 1
    prev_digit = s[0]
    for i in range(1, len(s)):
        if s[i] == prev_digit:
            curr_count += 1
        else:
            encoded.append(f"{curr_count}{prev_digit}")
            curr_count = 1
            prev_digit = s[i]
    
    if curr_count > 0:
        encoded.append(f"{curr_count}{prev_digit}")
    
    return "".join(encoded)
class Solution:
    def countAndSay(self, n: int) -> str:
        curr_rle = "1"

        for i in range(n-1):
            curr_rle = run_length_encode(curr_rle)
        return curr_rle
        
        
# @lc code=end


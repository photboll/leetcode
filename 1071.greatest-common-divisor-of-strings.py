#
# @lc app=leetcode id=1071 lang=python3
#
# [1071] Greatest Common Divisor of Strings
#

# @lc code=start
class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        #The substrings length must be a divisor of both m and n 
        m = len(str1)
        n = len(str2)
        for substr_len in range(n, 0, -1):
            #print(substr_len, m, n)
            if m % substr_len== 0 and n % substr_len == 0:
                #check if the prefix of str2 with this length is a divisor
                substr = str2[:substr_len]
                #print(substr)
                if substr * (m // substr_len) == str1 and substr * (n // substr_len) == str2:
                    return substr
        return ""

        
# @lc code=end


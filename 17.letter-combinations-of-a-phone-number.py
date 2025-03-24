#
# @lc app=leetcode id=17 lang=python3
#
# [17] Letter Combinations of a Phone Number
#

# @lc code=start
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        itoas = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl", 
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        } 
        
        if len(digits) == 0:
            return []
        result = []
        def backtrack(i, letters):
            if i == len(digits):
                result.append("".join(letters))
                return 
            
            for char in itoas[digits[i]]:
                letters.append(char)
                backtrack(i+1, letters)
                letters.pop()
        backtrack(0, [])
        return result 
# @lc code=end


#
# @lc app=leetcode id=1295 lang=python3
#
# [1295] Find Numbers with Even Number of Digits
#

# @lc code=start
def even_number_of_digits(x):
    is_even = False
    while x > 9:
        x //= 10
        is_even = not is_even
    return is_even
class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        count = 0
        for num in nums:
            if even_number_of_digits(num):
                count += 1
        return count
        
# @lc code=end


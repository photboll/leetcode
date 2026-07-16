#
# @lc app=leetcode id=1291 lang=python3
#
# [1291] Sequential Digits
#

# @lc code=start
class Solution:
    sequential_nums = [i for i in range(1, 10)]
    for num in sequential_nums:
        d = num % 10#the last digit 
        if d < 9:#if a larger single digit exists. append it to num and add it to the list
            sequential_nums.append(num*10 + d + 1)

    def sequentialDigits(self, low: int, high: int) -> List[int]:
        return [num for num in self.sequential_nums if low <= num <= high]


        
# @lc code=end


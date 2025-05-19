#
# @lc app=leetcode id=3024 lang=python3
#
# [3024] Type of Triangle
#

# @lc code=start
def is_triangle(a, b, c):
    return (a + b > c) and (b+c > a) and (a+c > b)

class Solution:
    def triangleType(self, nums: List[int]) -> str:
        if not is_triangle(nums[0], nums[1], nums[2]):
            return "none"
        elif nums[0] == nums[1] == nums[2]:
            return "equilateral"
        elif ((nums[0] == nums[1]) or
              (nums[1] == nums[2]) or
              (nums[0] == nums[2])):
            return "isosceles"
        else:
            return "scalene"
        
# @lc code=end


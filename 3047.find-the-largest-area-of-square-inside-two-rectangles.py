#
# @lc app=leetcode id=3047 lang=python3
#
# [3047] Find the Largest Area of Square Inside Two Rectangles
#

# @lc code=start
def interval_overlap(a1, a2, b1, b2):
    lo = max(a1, b1)
    hi = min(a2, b2)
    if lo >= hi:
        return None
    return lo, hi

def rectangle_overlap(ax1: int, ay1: int, ax2: int, ay2: int, bx1: int, by1: int, bx2: int, by2: int):
    x_interval = interval_overlap(ax1, ax2, bx1, bx2)
    if x_interval is None:
        return None

    y_interval = interval_overlap(ay1, ay2, by1, by2)
    if y_interval is None:
        return None
    
    return x_interval[0], y_interval[0], x_interval[1], y_interval[1]

def area_largest_square_in_rectangle(x1: int, y1: int, x2: int, y2: int):
    width = x2 - x1
    height = y2 - y1
    return min(width, height)**2

class Solution:
    def largestSquareArea(self, bottomLeft: List[List[int]], topRight: List[List[int]]) -> int:
        n = len(bottomLeft)

        result = 0
        for i in range(n):
            rect_a = (*bottomLeft[i], *topRight[i])
            for j in range(i+1, n):
                rect_b = (*bottomLeft[j], *topRight[j])
                rect_overlap = rectangle_overlap(*rect_a, *rect_b)
                if rect_overlap is None:
                    continue
                result = max(
                    result,
                    area_largest_square_in_rectangle(*rect_overlap)
                )
        return result

            


        
# @lc code=end


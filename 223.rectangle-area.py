#
# @lc app=leetcode id=223 lang=python3
#
# [223] Rectangle Area
#

# @lc code=start
def swap(ax1: int, ay1: int, ax2: int, ay2: int, bx1: int, by1: int, bx2: int, by2: int):
    return (bx1, by1, bx2, by2, ax1, ay1, ax2, ay2)

class Solution:
    def computeArea(self, ax1: int, ay1: int, ax2: int, ay2: int, bx1: int, by1: int, bx2: int, by2: int) -> int:
        
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
        
        def rectangle_area(x1: int, y1: int, x2: int, y2: int):
            width = x2 - x1
            height = y2 - y1
            return width * height
        
        area_a = rectangle_area(ax1, ay1, ax2, ay2)
        area_b = rectangle_area(bx1, by1, bx2, by2)
        overlap = rectangle_overlap(ax1, ay1, ax2, ay2, bx1, by1, bx2, by2)
        if overlap is None:
            overlapping_area = 0
        else:
            overlapping_area = rectangle_area(*overlap)
        return area_a + area_b - overlapping_area
    
class SolutionV1:
    def computeArea(self, ax1: int, ay1: int, ax2: int, ay2: int, bx1: int, by1: int, bx2: int, by2: int) -> int:
        """  
        First we consider 1D, overlapping intervals,
        Do i want to relabel them in anyway, like a always being the leftmost
        if ax1 is always the leftmost. then we have two cases of ovelap
        1. bx1 <= ax2 and bx2 <= ax2: bx1 to bx2 is the overlapping interval, b is contained in a
        2. bx1 <= ax2 and bx2 > ax2: bx1 to ax2 is the overlapping interval. 
        ax1, ax2, bx1 and bx2
        
        ax2 < bx1 : No overlap 
        
        """
        
        def interval_intersect(a1, a2, b1, b2):
            # interval [a1, a2] interesect [b1, b2]
            if b1 < a1:
                # we want interval a to be the leftmost interval 
                #so swap them
                a1, b1 = b1, a1
                a2, b2 = b2, a2
            
            if b1 <= a2 and b2 <= a2:
                return b1, b2
            elif b1 <= a2:
                return b1, a2
            else:
                return None
        
        def rectangle_intersect(ax1: int, ay1: int, ax2: int, ay2: int, bx1: int, by1: int, bx2: int, by2: int):
            x_interval = interval_intersect(ax1, ax2, bx1, bx2)
            if x_interval is None:
                return None

            y_interval = interval_intersect(ay1, ay2, by1, by2)
            if y_interval is None:
                return None
            
            return (x_interval[0], y_interval[0]), (x_interval[1], y_interval[1])

        def rectangle_overlap_area(ax1: int, ay1: int, ax2: int, ay2: int, bx1: int, by1: int, bx2: int, by2: int):
            overlap = rectangle_intersect(ax1, ay1, ax2, ay2, bx1, by1, bx2, by2)
            if overlap is None:
                return 0
            #print(overlap)
            return rectangle_area(*overlap[0], *overlap[1])
        
        def rectangle_area(x1: int, y1: int, x2: int, y2: int):
            width = x2 - x1
            height = y2 - y1
            return width * height
        
        area_a = rectangle_area(ax1, ay1, ax2, ay2)
        area_b = rectangle_area(bx1, by1, bx2, by2)
        overlapping_area = rectangle_overlap_area(ax1, ay1, ax2, ay2, bx1, by1, bx2, by2)
        return area_a + area_b - overlapping_area
        
        
        
        

        
# @lc code=end


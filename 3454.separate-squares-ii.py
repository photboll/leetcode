#
# @lc app=leetcode id=3454 lang=python3
#
# [3454] Separate Squares II
#

# @lc code=start
class Solution:
    def separateSquares(self, squares: List[List[int]]) -> float:
        
        events = []
        for x, y, l in squares:
            events.append((y, 1, x, x+l))
            events.append((y+l, -1, x, x+l))
        
        events.sort()
        xs = []
        prev_y = events[0][0]
        total = 0
        areas = []
        
        def union(intervals):
            intervals.sort()
            res = cur= 0
            end = -1e30
            for a,b in intervals:
                if a > end:
                    res += b-a
                    end = b
                elif b > end:
                    res += b -end
                    end = b
            return res
        
        for y, type, x1, x2 in events:
            if y > prev_y and xs:
                h = y - prev_y
                w = union(xs)
                areas.append((prev_y, h, w))
                total += h * w
            if type ==1:
                xs.append((x1, x2))
            else:
                xs.remove((x1, x2))
            prev_y = y
        
        target = total /2
        area_below = 0
        for y, h, w in areas:
            if area_below + h * w >= target:
                return y + (target - area_below)/w
            area_below += h * w

        return 0.0
        
# @lc code=end


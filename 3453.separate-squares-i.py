#
# @lc app=leetcode id=3453 lang=python3
#
# [3453] Separate Squares I
#

# @lc code=start
class Solution:
    def separateSquares(self, squares: List[List[int]]) -> float:
        """
        line sweep? 
        can i find a function f(y) that describes the total area below y?
        
        binary search on y? is it fast enough to check 
        
        we always have three types of squares.
        1. sqaures completely below the line
        2. squares completely above the line
        3. squares intersected by the line 
        
        """
        
        def area_below(y_hat):
            total = 0
            for _, y, l in squares:
                if y + l < y_hat:#the square is completely below
                    total += l*l
                elif y <= y_hat <= y+l:#the square intersects y_hat
                    #only the part below counts 
                    total += l * (y_hat - y)
            return total
        
        low = squares[0][1]
        high = squares[0][1]
        for _, y, l in squares:
            low = min(low, y)
            high = max(high, y+l)

        target = area_below(high) / 2
        
        while (high - low) > 1e-6:
            mid = (high + low) / 2
            if area_below(mid) < target:
                low = mid
            else:
                high = mid
        return (low + high ) /2 



                
                    
        
# @lc code=end


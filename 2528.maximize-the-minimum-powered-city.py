#
# @lc app=leetcode id=2528 lang=python3
#
# [2528] Maximize the Minimum Powered City
#

# @lc code=start
class Solution:
    def maxPower(self, stations: List[int], r: int, k: int) -> int:

        n = len(stations)

        def is_possible(target_power):
            additions = [0] * n
            stations_used = 0

            window_sum = sum(stations[j] for j in range(min(n, r)))
            
            for i in range(n):
                
                if i + r < n:
                    window_sum += stations[i+r] + additions[i+r]

                if window_sum < target_power:
                    deficit = target_power - window_sum
                
                    stations_used += deficit
                    if stations_used > k:
                        return False
                    
                    placesment_idx = min(n-1, i+r)
                    additions[placesment_idx] += deficit

                    window_sum += deficit
                    

            
                if i - r >= 0:
                    window_sum -= stations[i-r] + additions[i-r]
            return True
            
        
        low = 0
        high = sum(stations) + k
        res = 0
        
        while low <= high:
            mid = low + (high - low) // 2

            if is_possible(mid):
                res = mid
                low = mid + 1
            else:
                high = mid - 1
        
        return res
            
        
# @lc code=end


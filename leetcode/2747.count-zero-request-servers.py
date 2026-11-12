# @lc app=leetcode id=2747 slug=count-zero-request-servers lang=python3
#
# [2747] Count Zero Request Servers
# Difficulty: Medium
# Tags: Array, Hash Table, Sliding Window, Sorting
# URL: https://leetcode.com/problems/count-zero-request-servers/
#
# @lc code=start
class Solution:
    def countServers(self, n: int, logs: List[List[int]], x: int, queries: List[int]) -> List[int]:
        logs.sort(key= lambda x: x[1])
        queries = sorted((t, i) for i, t in enumerate(queries))

        result = [0] * len(queries)
        counts = [0] * (n+1)
        l = r = active = 0

        for t, i in queries:
            #t is the current time
            while r < len(logs) and logs[r][1] <= t:
                srv_id = logs[r][0]
                if counts[srv_id] == 0:
                    active += 1
                counts[srv_id] += 1
                r += 1
            
            #remove those leaving the window
            while l < r and logs[l][1] < t - x:
                srv_id = logs[l][0]
                counts[srv_id] -= 1
                if counts[srv_id] == 0:
                    active -= 1
                
                l += 1


            result[i] = n - active

        return result
                
                


                    


            
            
        
        

# @lc code=end

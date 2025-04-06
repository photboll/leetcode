#
# @lc app=leetcode id=134 lang=python3
#
# [134] Gas Station
#

# @lc code=start
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n = len(gas)
        i = 0
        while i < n:
            target = (i+ n)
            cur_gas = 0
            start = i

            #Keep driving as long as we have fuel
            while  cur_gas >= 0:
                if i == target:
                    return start
                cur_gas += gas[i % n]#Fill the tank with all available fuel
                cur_gas -= cost[i % n]#Drive to the next gas station
                i += 1
        return -1
                
        
# @lc code=end


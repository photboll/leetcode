#
# @lc app=leetcode id=2145 lang=python3
#
# [2145] Count the Hidden Sequences
#

# @lc code=start
class Solution:
    def numberOfArrays(self, differences: List[int], lower: int, upper: int) -> int:
        #we ned to find the interval ofhte differnces,
        #suppose we start the sequence with a cur_value = 0
        #we then traverse the differences array modifying cu value acording to each difference
        #We need to keep track of the minimum and maximum cur_value seen during this simulation
        #then we translate sequnce so that lower == minimum , upper - max should then give us the answer 
        cur_value = 0
        min_value =  cur_value
        max_value =  cur_value
        for diff in differences:
            cur_value += diff
            min_value = min(min_value, cur_value)
            max_value = max(max_value, cur_value)
            
        seq_range = max_value - min_value
        
        count_possible = (upper - lower) - seq_range + 1 #+1 since it is including the endpoint
        #Negative counts means that the interval need to be expanded by the count to fit a single sequence
        #print(min_value, max_value, seq_range, count_possible)
        return max(count_possible, 0)
        
# @lc code=end


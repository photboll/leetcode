#
# @lc app=leetcode id=3445 lang=python3
#
# [3445] Maximum Difference Between Even and Odd Frequency II
#

# @lc code=start
class Solution:
    def maxDifference(self, s: str, k: int) -> int:
        """
        i missunderstood the task. it is at least size of k, not at most
        Sliding window won't work directly
        Can we flip it?
        or should we do something like a prefix_sum, but it requires keeping track of all char counts
        the constraints only allow 5 unique chars
        What is necessary for us to even consider checking if the difference have changed?
        Window size must be at least k.
        At least one even frequenct in the window
        At least one odd frequency in the window
        
        We also now that this changes at each step of the sliding.
        
        How do we incorporate the prefix sum?
        do we need to keep track of the counts of all chars for every possible endinf index?
        Are we focred to select a and b such that a is maximized and b is minimized?
        is it sufficent to onlu keep track of maximum difference by frea[a] - freq[b]?
        NO, we cant find the frequency of any char if we do. 
        
        What if we use a structure like prefix[is_even][index][char]
        
        """
        def get_status(count_a, count_b):
            return ((count_a & 1) << 1) | (count_b & 1) 
        
        n = len(s)
        ans = float("-inf")
        for a in "01234":
            for b in "01234":
                if a == b:
                    continue

                best = [float("inf")] * 4
                count_a = count_b = 0
                prev_a = prev_b = 0
                left = -1
                
                for right in range(n):
                    count_a += s[right] == a
                    count_b += s[right] == b
                    
                    while right - left >= k and count_b - prev_b >= 2:
                        left_status = get_status(prev_a, prev_b)
                        best[left_status] = min(best[left_status], prev_a - prev_b)
                    
                        left += 1
                        prev_a +=  s[left] == a
                        prev_b += s[left] == b


                    right_status = get_status(count_a, count_b)
                    if best[right_status ^ 0b10] != float("inf"):
                        ans = max(
                            ans, count_a - count_b - best[right_status ^ 0b10]
                            
                        )
        if ans == float("-inf"):
            return -1
        
        return ans
# @lc code=end


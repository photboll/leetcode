#
# @lc app=leetcode id=3480 lang=python3
#
# [3480] Maximize Subarrays After Removing One Conflicting Pair
#

# @lc code=start
class Solution:
    def maxSubarrays(self, n: int, conflictingPairs: List[List[int]]) -> int:
        """
        We want to maximize the number of subarrays
        Same as minimize the number of pairs removed due to conflict 
        there are no duplicates in num and no missing values. does this not imply that which pair we remove does not make a difference?
        assuming that the pairs in conflicting pairs are disjoint. 
        This is obviously not guaranteed, in the second two different pairs have a 5 (same for 2)in them.
        
        ANy way we will want to remove the conflictingPair that maximizes the number of affected subarays.
        We frame each conflicting pair as an edge in a graph.
        The weight of the edge is the number of subarrays which contain both node.
        we should then remove the heaviest edge in order to minimze the, no all edges will have the same weight due to symmetry
        we are back to that we can choose to remove any edge freely.
        I AM STUPID, i have been looking at the subsequence version of the problem.
        """
        
        right = [[] for _ in range(n+1)]
        for a, b in conflictingPairs:
            right[max(a, b)].append(min(a, b))
            
        result = 0
        left = [0, 0]
        #bonus[u] is the total score gained if the conflict removing u is removed
        bonus = [0] * (n+1)

        #r is the 
        for r in  range(1, n+1):
            for l in right[r]:
                if l > left[0]:
                    left = [l, left[0]]
                elif l> left[1]:
                    left = [left[0], l]
            
            result += r - left[0]
            
            if left[0] > 0:
                bonus[left[0]] += left[0] - left[1]
        
        return result + max(bonus)
    
    def maxSubarrays(self, n: int, conflictingPairs: List[List[int]], k: int):
        """
        extends maxSubarrays to get the answer where we are allowed to delete upto k conflictingPairs
        """
        pass

        
        
        
# @lc code=end


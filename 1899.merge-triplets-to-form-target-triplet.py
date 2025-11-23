#
# @lc app=leetcode id=1899 lang=pythonk
#
# [1899] Merge Triplets to Form Target Triplet
#

# @lc code=start
class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        """
        max is increasing so a < x for it to be possilble 
        we only car about triplets that contain one fo the target elements 
        using any other triplet will not move us to the target
        we can fix it position by position 
        if we have two valid candidates to fix a position which one should we pick?
        the one with the smallest values in the other positions 
        if the other positions contains a value larger than the one in target.
        using it would put is in a unrecoverable situation
        """
        triplets = set(tuple(trip) for trip in triplets)
        k = 3
        fixed = [False] * k
        for triplet in triplets:
            #A triplet is useful if one of the position matches the target
            #and the other two positions are less than or equal to its target
            useful = True
            fixes = [False] * k
            for i in range(k):
                if triplet[i] > target[i]:
                    useful = False
                    break
                elif triplet[i] == target[i]:
                    fixes[i] = True
            if useful:
                for i in range(k):
                    fixed[i] |= fixes[i]
                if all(fixed):
                    return True
        return False
                
                    



        
# @lc code=end


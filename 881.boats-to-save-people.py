#
# @lc app=leetcode id=881 lang=python3
#
# [881] Boats to Save People
#

# @lc code=start
class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        """
        at most two people in each boat
        implies that any spare capacity of a boat can not be utilized
        Can the current heaviset person share a boat with anyone?
        it suffices to check the current lightest person.
        if they togehter exceed the capacity, the haveiest needs their own boat
        
        
        """
        people.sort()
        l = 0
        r = len(people) - 1
        res = 0
        while l < r:
            #lightest + heaviest exceeds capacity?
            if people[l] + people[r] > limit:
                #heavy gets their own boat
                res += 1
                r -= 1
            else:
                #they share a boat
                res += 1
                l += 1
                r -= 1
        
        if l == r:
            #one person left to get a boat 
            res += 1
        return res
        
# @lc code=end


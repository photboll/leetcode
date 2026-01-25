#
# @lc app=leetcode id=846 lang=python3
#
# [846] Hand of Straights
#

# @lc code=start
from collections import Counter
class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        hand.sort()
        freqs = Counter(hand)

        for num in hand:
            if freqs[num] > 0:
                #print(num, num+k, freqs)
                for i in range(num, num+groupSize):
                    freqs[i] -= 1
                    if freqs[i] < 0:
                        return False
        return True
        
# @lc code=end


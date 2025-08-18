#
# @lc app=leetcode id=679 lang=python3
#
# [679] 24 Game
#

# @lc code=start
from fractions import Fraction
class Solution:
    def judgePoint24(self, cards: List[int]) -> bool:
        """
        Need to evaluate all possible expression trees.
        There is only 9 ** 4 possible inputs to the function. So less than 10k inputs
        pracically even less since the order does not matter only the frequency of the cards

        can we do it using dp and or backtracking?
        
        + and * are commutative we only need to consider one cur + card[i] 
        - and / are not commutative we need to consider both cur - card[i] and card[i] - cur

        """
        
        def backtrack(nums):
            if len(nums) == 1 and nums[0] == 24:
                return True
            
            n = len(nums)
            for i in range(n):
                for j in range(i+1, n):
                    rest = [nums[k] for k in range(n) if k!=i and k != j]
                    a,b = nums[i], nums[j]

                    cands = []
                    cands.append(a+b)
                    cands.append(a*b)
                    cands.append(a-b)
                    cands.append(b-a)
                    if b > 0:
                        cands.append(Fraction(a, b))
                    if a > 0:
                        cands.append(Fraction(b, a))

                    for cand in cands:
                        if backtrack(rest + [cand]):
                            return True
            return False
        
        return backtrack(cards)
            
            

        
# @lc code=end


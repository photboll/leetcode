#
# @lc app=leetcode id=2260 lang=python3
#
# [2260] Minimum Consecutive Cards to Pick Up
#

# @lc code=start
class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        #This is equivalent to finding the shortest distance between duplicate values
        min_cards = float("inf")
        prev_pos = {}
        for i, card in enumerate(cards):
            if card in prev_pos:
                #Consider the streak of starting at te prevposition upto this
                min_cards = min(min_cards, i - prev_pos[card]+1)
            prev_pos[card] = i
        if min_cards == float("inf"):
            return -1
        
        return min_cards
# @lc code=end


#
# @lc app=leetcode id=1927 lang=python3
#
# [1927] Sum Game
#

# @lc code=start
class Solution:
    def sumGame(self, num: str) -> bool:
        n = len(num)
        print(num)

        def sum_and_count_qs(chars):
            s = q = 0
            for char in chars:
                if char == "?":
                    q += 1
                else:
                    s += int(char)
            return s, q
        
        left_s, left_q = sum_and_count_qs(num[:n//2])
        right_s, right_q = sum_and_count_qs(num[n//2:])

        return (left_q + right_q) % 2 == 1 or left_s - right_s != (right_q - left_q) * 9 //2
        


class Solution_scrapped:
    def sumGame(self, num: str) -> bool:
        """
        Alice want to make the gap wider
        Bob want to close the gap
        we only have positive numbers 
        the order of the numbers and ? does not matter
        no wait, i dont have to keep track of both sums 
        i can just keep track of the difference
        i think this would be linear scan problem then 
        waht about the question marks? those i have to have the absolute counts for
        """
        n = len(num)
        #
        diff = 0
        left_q = 0# number of question marks left 
        right_q = 0
        for i, char in enumerate(num):
            second_half = i %(n//2)
            if char == "?" and second_half:
                right_q += 1
            elif char == "?":
                left_q += 1
            elif second_half:
                diff -= int(char)
            else:
                diff += int(char)

        def dp(player, diff, lq_rem, rq_rem):
            if lq_rem == 0 and rq_rem == 0:
                return diff != 0
            
            if player:#it is Bobs turn
                #make a left question mark into a number
                pass
                #make a right question mark into number








        
        
# @lc code=end


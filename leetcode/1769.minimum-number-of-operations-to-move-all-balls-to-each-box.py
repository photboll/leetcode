# @lc app=leetcode id=1769 slug=minimum-number-of-operations-to-move-all-balls-to-each-box lang=python3
#
# [1769] Minimum Number of Operations to Move All Balls to Each Box
# Difficulty: Medium
# Tags: Array, String, Prefix Sum
# URL: https://leetcode.com/problems/minimum-number-of-operations-to-move-all-balls-to-each-box/
#
# @lc code=start
class Solution:
    def minOperations(self, boxes: str) -> list[int]:
        """
         a forward and a backward pass
         each pass moves all balls in that direction 
         answer will be forward[i] + backward[i]
        """
        n = len(boxes)
        answer = [0] * n
        balls = int(boxes[0])
        cost = 0

        for i in range(1, n):
            #move all current balls one step forward 
            #+ the solution for i-1 
            cost += balls
            answer[i] += cost
            if boxes[i] == "1":
                balls += 1
        
        #backwards
        balls = int(boxes[-1])
        cost = 0
        for i in range(n-2,-1, -1):
            cost += balls
            answer[i] += cost
            if boxes[i] == "1":
                balls += 1

        return answer

            
            


        
        
        

# @lc code=end

# @lc app=leetcode id=2058 slug=find-the-minimum-and-maximum-number-of-nodes-between-critical-points lang=python3
#
# [2058] Find the Minimum and Maximum Number of Nodes Between Critical Points
# Difficulty: Medium
# Tags: Linked List
# URL: https://leetcode.com/problems/find-the-minimum-and-maximum-number-of-nodes-between-critical-points/
#
# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:

        #local maxima/minima cant exist for idx 0
        idx = 1
        prev = head
        curr = head.next
        min_dist = float("inf")
        max_dist = -1
        prev_idx = None
        first_idx = None

        while curr.next:
            nxt = curr.next

            #a point cant be max and min at the saame time
            if ((prev.val < curr.val > nxt.val) or (#maxima
                 prev.val > curr.val < nxt.val#minima
            )):
                if prev_idx and idx - prev_idx < min_dist:
                    min_dist = idx - prev_idx
                
                if not first_idx:
                    first_idx = idx
                elif idx - first_idx > max_dist:
                    max_dist = idx - first_idx

                prev_idx = idx

            idx += 1
            prev = curr
            curr = nxt 
        
        if min_dist == float("inf"):
            min_dist = -1
    
        return [min_dist, max_dist]


        

# @lc code=end

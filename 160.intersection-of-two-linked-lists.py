#
# @lc app=leetcode id=160 lang=python3
#
# [160] Intersection of Two Linked Lists
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        countA = 1
        a = headA
        while a is not None:
            countA += 1
            a = a.next
        
        countB = 1
        b = headB
        while b is not None:
            countB += 1
            b = b.next
        #Let A be the longer one 
        if countB > countA:
            headA, headB = headB, headA
            countA, countB = countB, countA
        
        #Advance the longer one so the emainders are equal length 
        a = headA
        while headA is not None and countA > countB:
            countA -= 1
            a = a.next
        
        #Advance them in pairs until we arrive at the same element 
        b = headB
        while headA is not None:
            if a == b:
                return a
            a = a.next
            b = b.next
        
        return None
# @lc code=end


#
# @lc app=leetcode id=86 lang=python3
#
# [86] Partition List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        lessThen = ListNode()
        greqThen = ListNode()
        dummyLT = lessThen
        dummyGT = greqThen
         
        curr = head
        while curr:
            if curr.val < x:
                lessThen.next = curr
                lessThen = curr
            else:
                greqThen.next = curr
                greqThen = curr
                
            curr = curr.next       

        greqThen.next = None
        lessThen.next = dummyGT.next
        
        return dummyLT.next
# @lc code=end


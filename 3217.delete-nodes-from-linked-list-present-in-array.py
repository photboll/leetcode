#
# @lc app=leetcode id=3217 lang=python3
#
# [3217] Delete Nodes From Linked List Present in Array
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head
        forbidden = set(nums)   
        prev = dummy
        curr = head
        
        while curr:
            if curr.val in forbidden:
                prev.next = curr.next
            else:
                prev = curr
            curr = curr.next

        return dummy.next
            
        
    


        
# @lc code=end


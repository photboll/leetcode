#
# @lc app=leetcode id=328 lang=python3
#
# [328] Odd Even Linked List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        We will walk thorugh the list, breaking each node of from the original list and adding it to either
        the odd linkedlist or the even linked list,
        then we stitch them together 
        """
        if not head or not head.next:
            return head

        odd = head
        even = head.next
        even_head = even 

        while even and even.next:
            #print(even.val)
            odd.next = even.next
            odd = odd.next
            
            even.next = odd.next
            even = even.next
            
        odd.next = even_head 
        return head
            
# @lc code=end


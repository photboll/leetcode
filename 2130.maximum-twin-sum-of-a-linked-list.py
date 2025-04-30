#
# @lc app=leetcode id=2130 lang=python3
#
# [2130] Maximum Twin Sum of a Linked List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
def max_pair_sum(head1, head2):
    max_sum = 0
    curr = head1
    pair = head2
    while curr and pair:
        max_sum = max(max_sum, curr.val + pair.val)
        #print(curr.val, pair.val)
        curr = curr.next
        pair = pair.next
    
    return max_sum
class Solution:

    def pairSum(self, head: Optional[ListNode]) -> int:
        """reverse the links for the second half of the linked list"""
        slow = head
        fast = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        prev = slow
        curr = slow.next
        prev.next = None
        while curr:
            next =curr.next
            curr.next = prev
            prev = curr
            curr = next
        
        return max_pair_sum(head, prev)
        
        
# @lc code=end


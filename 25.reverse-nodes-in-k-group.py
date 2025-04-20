#
# @lc app=leetcode id=25 lang=python3
#
# [25] Reverse Nodes in k-Group
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

def get_length(head):
    length = 0
    curr = head 
    while curr:
        length += 1
        curr = curr.next
    return length

def reverse_k(head, k):
    """
    Reverses the k first elements in the linked list of head 
    returns the new head of the revered segment and the old head now the tail 
    """
    prev = None
    curr = head
    while k>0 and curr:
        next = curr.next 
        curr.next = prev 
        prev = curr
        curr = next 
        k -= 1
    head.next = next
    #print(head.val, prev.val, curr.val)
    return prev, head 

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        n = get_length(head)
        num_groups = n // k
        new_head, end = reverse_k(head, k)
        for _ in range(num_groups-1):
            curr = end
            start, end = reverse_k(curr.next, k)
            curr.next = start
            
        return new_head
        
# @lc code=end


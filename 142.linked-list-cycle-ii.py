#
# @lc app=leetcode id=142 lang=python3
#
# [142] Linked List Cycle II
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:break
        else:
            return 
        while head != slow:
            head = head.next
            slow = slow.next
        return head
        
class SolutionV1:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Basic slow and fast wont work. as we are not guaranteed to meet at the start of the cycle.
        Doing slow and fast and varying the speed of fast, could work 
        we can then find the first node in the cycle by incrementally speeding up fast
        but this would take a very long time 
        
        if we know that there is a cycle. can we find the start?

        """
        if not head:
            return head
        visited = set()
        curr = head
        while curr.next:
            if curr in visited:
                return curr
            
            visited.add(curr)
            curr = curr.next

        
        
# @lc code=end


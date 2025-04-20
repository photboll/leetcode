#
# @lc app=leetcode id=23 lang=python3
#
# [23] Merge k Sorted Lists
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from heapq import heappush, heappop
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        k = len(lists)
        
        heap =[]#(value, list_index, current_head)
        for i in range(k):
            head = lists[i]
            if head :
                heappush(heap, (head.val, i, head))
        
        if not heap:
            return None
        
        _, i, merged_head = heappop(heap)
        if merged_head.next:
            next = merged_head.next 
            heappush(heap, (next.val, i, next)) 
            
        prev = merged_head
        while heap:
            _, i, curr = heappop(heap)
            prev.next = curr 
            if curr.next:
                next = curr.next
                heappush(heap, (next.val, i, next))
            prev = curr
    
        
        return merged_head
# @lc code=end


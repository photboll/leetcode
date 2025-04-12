#
# @lc app=leetcode id=148 lang=python3
#
# [148] Sort List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
def merge(l1, l2):
    """Takes two sorted linked lists and merges them into one"""
    dummy = ListNode()
    tail = dummy
    
    while l1 and l2:
        if l1.val < l2.val:
            tail.next = l1
            l1 = l1.next
        else:
            tail.next = l2
            l2 = l2.next
        tail = tail.next
    
    #Append the remaining longer list 
    if l1:
        tail.next = l1
    elif l2:
        tail.next = l2
    return dummy.next

def merge_sort(head):
    "Sorts the linked list in ascending order"
    if not head or not head.next:#
        #Empty and single element lists are always sorted
        return head
    #Split
    mid = get_middle(head)
    right = mid.next
    mid.next  = None#Break the list in halfs 

    #Sort each half
    left_sorted = merge_sort(head)
    right_sorted = merge_sort(right)
    #Merge 
    return merge(left_sorted, right_sorted)
    
def get_middle(head):
    """Find the middle element of linked List."""
    slow = head
    fast = head.next
    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next
    return slow
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        return merge_sort(head)
                 
        
# @lc code=end


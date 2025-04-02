#
# @lc app=leetcode id=109 lang=python3
#
# [109] Convert Sorted List to Binary Search Tree
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        def sortListToBSTRecur(head, length):
            if length == 0:
                return None
            if length == 1:
                return TreeNode(val=head.val)
            
            left_len = length // 2 
            right_len = length - left_len - 1
            curr = head
            for _ in range(left_len):
                curr = curr.next
            
            root = TreeNode(val=curr.val)
            root.left = sortListToBSTRecur(head, left_len)
            root.right = sortListToBSTRecur(curr.next, right_len)
            return root
        
        curr = head
        length = 0
        while curr:
            length += 1
            curr = curr.next
        
        return sortListToBSTRecur(head, length)
        
# @lc code=end


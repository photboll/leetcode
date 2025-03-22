package leetcode

/*
 * @lc app=leetcode id=83 lang=golang
 *
 * [83] Remove Duplicates from Sorted List
 */

// @lc code=start
/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
func deleteDuplicates(head *ListNode) *ListNode {
	if head == nil || head.Next == nil {
		return head
	}

	curr := head
	for curr != nil{
		if curr.Next != nil && curr.Val == curr.Next.Val{
			curr.Next = curr.Next.Next
		}else{
			curr = curr.Next
		}
	}
	return head
}

// @lc code=end

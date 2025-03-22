package leetcode

import "runtime/trace"

/*
 * @lc app=leetcode id=82 lang=golang
 *
 * [82] Remove Duplicates from Sorted List II
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
	dummy := &ListNode{Next: head}
	prev := dummy
	curr := head

	for curr != nil {
		hasDuplicates := false

		for curr.Next != nil && curr.Val == curr.Next.Val{
			curr = curr.Next
			hasDuplicates = true
		}

		if hasDuplicates{
			prev.Next = curr.Next
		}else {
			prev = prev.Next
		}
		curr = curr.Next
	}

	return dummy.Next
}

// @lc code=end

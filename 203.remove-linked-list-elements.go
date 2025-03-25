package leetcode
/*
 * @lc app=leetcode id=203 lang=golang
 *
 * [203] Remove Linked List Elements
 */

// @lc code=start
/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
func removeElements(head *ListNode, val int) *ListNode {
	dummy := &ListNode{Next:head}
	curr := head
	prev := dummy
	for curr != nil{
		if curr.Val == val{
			prev.Next = curr.Next
		}else {
			prev = curr
		}
		curr = curr.Next
	}
	return dummy.Next
}
// @lc code=end


package leetcode
/*
 * @lc app=leetcode id=19 lang=golang
 *
 * [19] Remove Nth Node From End of List
 */

// @lc code=start
/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
func removeNthFromEnd(head *ListNode, n int) *ListNode {
	dummy := &ListNode{Next: head}
    slow, fast := dummy, dummy
	//Let fast run ahead n elements 
	for i:= 0; i<=n;i++{
		fast = fast.Next
	}
	//Walk thtogh the list step by step in sync
	for fast != nil{
		slow = slow.Next
		fast = fast.Next
	}

	//Slow should now be right before the element to be removed
	slow.Next = slow.Next.Next

	return dummy.Next
}
// @lc code=end


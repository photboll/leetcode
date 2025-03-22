package leetcode

/*
 * @lc app=leetcode id=61 lang=golang
 *
 * [61] Rotate List
 */

// @lc code=start
/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
func rotateRight(head *ListNode, k int) *ListNode {
	if head == nil || head.Next == nil || k == 0 {
		return head
	}
	curr := head
	n := 0
	for curr != nil {
		n++
		curr = curr.Next
	}
	//Traverse it a second time
	var newHead *ListNode
	curr = head
	k= k % n
	if k == 0{
		return head
	}
	for curr != nil {
		n--
		if curr.Next == nil {
			curr.Next = head
			break
		}
		if n == k{ //This is the new end of the list
			tmp := curr.Next
			curr.Next = nil
			newHead = tmp
			curr = tmp
		} else {
			curr = curr.Next
		}

	}
	return newHead
}

// @lc code=end

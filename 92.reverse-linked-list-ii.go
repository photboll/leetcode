package leetcode

import "fmt"

/*
 * @lc app=leetcode id=92 lang=golang
 *
 * [92] Reverse Linked List II
 */

// @lc code=start
/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
//Moves along the list until right before the endPos
func advanceList(head *ListNode, curPos, endPos int) (*ListNode, int) {
	for curPos < endPos {
		head = head.Next
		curPos++
	}
	return head, curPos
}

// Returns the head of the remainiing listTail and the head and tail of the reversed portion
func reverseUntilEndPos(head *ListNode, curPos, endPos int) (*ListNode, *ListNode, *ListNode) {
	var prev, next *ListNode
	curr := head
	for head != nil {
		next = curr.Next
		curr.Next = prev
		if curPos == endPos {
			return next, curr, head
		}
		curPos++
		prev = curr
		curr = next
	}
	return nil, nil, nil
}
func reverseBetween(head *ListNode, left int, right int) *ListNode {
	if head == nil || head.Next == nil || left == right {
		return head
	}

	var prefixEnd, suffixHead, reversedHead, reversedTail *ListNode
	//advance to the end of the prefix
	dummy := &ListNode{Next:head}
	prefixEnd, currPos := advanceList(dummy, 0, left-1)
	suffixHead, reversedHead, reversedTail = reverseUntilEndPos(prefixEnd.Next, currPos+1, right)

	//Conect the prefix with the reversed portion
	prefixEnd.Next = reversedHead
	//connect the reversed tail with the suffixHead
	reversedTail.Next = suffixHead
	if left > 1 {
		return head
	} else {
		//When left is 1 then head will actually be the last element 
		return reversedHead
	}

}

// @lc code=end

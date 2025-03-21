package leetcode

/*
 * @lc app=leetcode id=116 lang=golang
 *
 * [116] Populating Next Right Pointers in Each Node
 */
// @lc code=start
/**
 * Definition for a Node.
 * type Node struct {
 *     Val int
 *     Left *Node
 *     Right *Node
 *     Next *Node
 * }
 */

func connect(root *Node) *Node {
	if root == nil{
		return root
	}

	if root.Next != nil && root.Right != nil{
		root.Right.Next = root.Next.Left
	}
	if root.Left != nil{
		root.Left.Next = root.Right
	}

	connect(root.Left)
	connect(root.Right)
	return root 
}
// @lc code=end


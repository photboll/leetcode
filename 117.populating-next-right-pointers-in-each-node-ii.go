package leetcode
/*
 * @lc app=leetcode id=117 lang=golang
 *
 * [117] Populating Next Right Pointers in Each Node II
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
func GetFirstChild(root *Node) *Node{
	for root != nil{
		if root.Left != nil{
			return root.Left
		}else if root.Right != nil{
			return root.Right
		}
		root = root.Next
	}
	return nil
}

func connect(root *Node) *Node {
	if root == nil {
		return root
	}
	//Need to be mindful of which children are missing 
	if root.Left != nil && root.Right != nil{
		root.Right.Next = GetFirstChild(root.Next)
		root.Left.Next = root.Right
	} else if root.Left != nil {//Only left child exists
		root.Left.Next = GetFirstChild(root.Next)
	} else if root.Right != nil {//Only right child exists 
		root.Right.Next = GetFirstChild(root.Next)
	}

	connect(root.Right)
	connect(root.Left)
	return root

}
// @lc code=end


/*
 * @lc app=leetcode id=114 lang=golang
 *
 * [114] Flatten Binary Tree to Linked List
 */

// @lc code=start
/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
 /*
 Flatten left child 
 flatten right child 
 as
 */
func flatten(root *TreeNode)  {
    flattenHelper(root)
}
//flattens the tree and returns the last element of the list
func flattenHelper(root *TreeNode) *TreeNode{
	if root == nil{
		return nil
	}

	//Flatten the left and right subtrees
	leftEnd := flattenHelper(root.Left)
	rightEnd := flattenHelper(root.Right)

	if leftEnd != nil{
		leftEnd.Right = root.Right //move the Right subtree to the end
		root.Right = root.Left //Move the original left subtree to the right child
		root.Left = nil
	}
	
	//Return the last element of the list 
	if rightEnd != nil{
		return rightEnd
	} else if leftEnd != nil {
		return leftEnd 
	}
	return root
	

}
// @lc code=end


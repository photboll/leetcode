/*
 * @lc app=leetcode id=112 lang=golang
 *
 * [112] Path Sum
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
func hasPathSum(root *TreeNode, targetSum int) bool {
	if root == nil{
		return false
	}

	if root.Left == nil && root.Right== nil{
		//Current node is a leaf node 
		//Base case: if root.val == targetSum
		return root.Val == targetSum
	}
	return hasPathSum(root.Left, targetSum - root.Val) || hasPathSum(root.Right, targetSum - root.Val)

}
// @lc code=end


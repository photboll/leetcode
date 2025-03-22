package leetcode

import "math"

/*
 * @lc app=leetcode id=124 lang=golang
 *
 * [124] Binary Tree Maximum Path Sum
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
//Returns the maximum path sum ending at root 
func maxPathSumRecur(root *TreeNode, res *int) int{
	//The non-empty constraint implies that the max sum might be negative 
	if root.Left == nil && root.Right == nil{
		*res = max(*res, root.Val)
		return root.Val
	}
	leftMax := math.MinInt
	rightMax := math.MinInt
	if root.Left != nil{
		leftMax = maxPathSumRecur(root.Left, res)
	}
	if root.Right != nil{
		rightMax = maxPathSumRecur(root.Right, res)
	}
	leftMax = max(leftMax, 0)
	rightMax = max(rightMax, 0)

	maxSum := leftMax + root.Val//The max is located in the left subtree
	maxSum = max(maxSum, rightMax + root.Val)//The max is located in the right subtree
	*res = max(*res, maxSum)
	//The path can connect the two halfs as well
	//But this path does not end at root so we can not return it 
	*res = max(*res, leftMax + rightMax + root.Val)
	return maxSum

}
func maxPathSum(root *TreeNode) int {
    //The path is either:
	//entirely within the left subtree,
	//entirely within the right subtree
	//Or it passes through the current node
	if root == nil{
		return 0
	}
	res := math.MinInt
	maxPathSumRecur(root, &res)
	return res
}
// @lc code=end


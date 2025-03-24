package leetcode

import "math"

/*
 * @lc app=leetcode id=110 lang=golang
 *
 * [110] Balanced Binary Tree
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
func abs(x int) int{
	if x < 0{
		return -x
	}
	return x
}
func checkHeight(root *TreeNode) (int, bool) {
	if root == nil {
		return 0, true
	}

	leftHeight, leftBalanced := checkHeight(root.Left)
	rightHeight, rightBalanced := checkHeight(root.Right)

	if !leftBalanced || !rightBalanced || abs(leftHeight-rightHeight) > 1 {
		return -1, false
	}

	return 1 + max(leftHeight, rightHeight), true
}

func isBalanced(root *TreeNode) bool {
	_, balanced := checkHeight(root)
	return balanced
}
// @lc code=end


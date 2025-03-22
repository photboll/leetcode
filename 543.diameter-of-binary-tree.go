package leetcode
/*
 * @lc app=leetcode id=543 lang=golang
 *
 * [543] Diameter of Binary Tree
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
func diameterRecur(root *TreeNode, res *int) int{
	if root == nil{
		return 0
	}
	leftHeight := diameterRecur(root.Left, res)
	rightHeight := diameterRecur(root.Right, res)

	*res = max(*res, leftHeight + rightHeight )

	return 1 + max(leftHeight, rightHeight)
}
func diameterOfBinaryTree(root *TreeNode) int {
   res := 0
   diameterRecur(root, &res)
   return res
}
// @lc code=end


package leetcode
/*
 * @lc app=leetcode id=106 lang=golang
 *
 * [106] Construct Binary Tree from Inorder and Postorder Traversal
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
 inorder = [left_subtree..., root, right_subtree...]
 postorder = [left_subtree..., right_subtree..., root]
 */
func buildTree(inorder []int, postorder []int) *TreeNode {
	if len(inorder) == 0{
		return nil
	} 
	n := len(postorder)
	root := &TreeNode{Val: postorder[n - 1]}
	sizeLeft := slices.Index(inorder, root.Val)
	root.Left = buildTree(inorder[:sizeLeft], postorder[:sizeLeft])
	root.Right = buildTree(inorder[sizeLeft+1:] , postorder[sizeLeft: n - 1])

	return root
}
// @lc code=end


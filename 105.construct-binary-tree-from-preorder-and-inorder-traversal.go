package leetcode

import (
	"slices"
)

/*
 * @lc app=leetcode id=105 lang=golang
 *
 * [105] Construct Binary Tree from Preorder and Inorder Traversal
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
 the first element of the preorder is always the root.
 The position of the root element in inorder splits the tree in two.
 So all elements before the root belongs to the left subtree and all elements after to the right subtree
 preroder = [root, left_subtree..., right_subtree...]
 inorder = [left_subtree..., root, right_subtree]
*/
func buildTree(preorder []int, inorder []int) *TreeNode {
	if len(preorder) < 1 {
		//Both lists should always have the same length so no need to check both
		return nil
	}
	root := &TreeNode{Val: preorder[0]}
	sizeLeft := slices.Index(inorder, root.Val)
	
	root.Left = buildTree(preorder[1:sizeLeft+1], inorder[:sizeLeft])
	root.Right = buildTree(preorder[sizeLeft + 1:], inorder[sizeLeft + 1:])
	
	return root
}

// @lc code=end

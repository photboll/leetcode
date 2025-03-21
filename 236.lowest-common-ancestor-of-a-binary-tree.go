package leetcode
/*
 * @lc app=leetcode id=236 lang=golang
 *
 * [236] Lowest Common Ancestor of a Binary Tree
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

 func lcaHelper(root, p, q *TreeNode) *TreeNode{
	if root == nil || root == p || root == q{
		return root
	}

	//check left and right subtree for ancestors
	l := lcaHelper(root.Left, p, q)
	r := lcaHelper(root.Right, p, q)

	if l == nil{
		return r
	} else if r == nil{
		return l
	} else {
		// We found p and q in either subtree
		//So the root is the LCA
		return root
	}
	
 }

 func lowestCommonAncestor(root, p, q *TreeNode) *TreeNode {
	return lcaHelper(root, p, q)
}
// @lc code=end


/*
 * @lc app=leetcode id=222 lang=golang
 *
 * [222] Count Complete Tree Nodes
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
func countNodes(root *TreeNode) int {
	count := 0
	countNodesHelper(root, &count)
	return count
}
func countNodesHelper(root *TreeNode, count *int){
	if root == nil{
		return
	}
	*count = *count + 1
	countNodesHelper(root.Left, count)
	countNodesHelper(root.Right, count)

}
// @lc code=end


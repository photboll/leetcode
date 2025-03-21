/*
 * @lc app=leetcode id=129 lang=golang
 *
 * [129] Sum Root to Leaf Numbers
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
func sumNumbers(root *TreeNode) int {
	return sumNumbersHelper(root, 0)

}
func sumNumbersHelper(root *TreeNode, num int) int {
	if root == nil {
		return 0
	}

	if root.Left == nil && root.Right == nil {
		//We are at a leaf node
		fmt.Println(10*num + root.Val)
		return 10*num + root.Val
	}
	leftSum := sumNumbersHelper(root.Left, 10*num+root.Val)
	rightSum := sumNumbersHelper(root.Right, 10*num+root.Val)
	return leftSum + rightSum
}

// @lc code=end


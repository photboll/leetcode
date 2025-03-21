package leetcode
/*

 * @lc app=leetcode id=107 lang=golang
 *
 * [107] Binary Tree Level Order Traversal II
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
func levelOrderBottom(root *TreeNode) [][]int {
    if root == nil{
		return nil
	}
	result := [][]int{}
	queue := []*TreeNode{root}

	for len(queue) > 0{
		curLevel := make([]int, len(queue))

		for i:= 0 ; i <  len(curLevel);i++{
			curr := queue[0]
			queue = queue[1:]
			curLevel[i] = curr.Val
			if curr.Left != nil{
				queue = append(queue, curr.Left)
			}
			if curr.Right != nil{
				queue = append(queue, curr.Right)
			}
		}
		result = append([][]int{curLevel}, result...)
	}
	return result
}
// @lc code=end


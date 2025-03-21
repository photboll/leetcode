package leetcode
/*
 * @lc app=leetcode id=103 lang=golang
 *
 * [103] Binary Tree Zigzag Level Order Traversal
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
func Reverese(slice []int){
	n := len(slice)
	for i:= 0; i < n / 2;i++{
		slice[i], slice[n-1-i] = slice[n-1-i], slice[i]
	}
}
func zigzagLevelOrder(root *TreeNode) [][]int {
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
		//if the current height is odd append the reverse of curLevel
		if len(result) % 2 == 1{
			Reverese(curLevel)
		}
		result = append(result, curLevel)
	}
	return result
}
// @lc code=end


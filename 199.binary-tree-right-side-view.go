package leetcode
/*
 * @lc app=leetcode id=199 lang=golang
 *
 * [199] Binary Tree Right Side View
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
type Entry struct{
	Node *TreeNode
	Level int 
}
func rightSideView(root *TreeNode) []int {
	queue := make([]*Entry, 1)
	queue[0] = &Entry{Node: root, Level: 0}
	ptr := 0
	result := []int{}
	for ptr < len(queue){
		curr := queue[ptr]
		ptr++
		if curr.Node == nil{
			continue
		}
		//check if next entry in queue has a higher level
		if ptr   == len(queue) || queue[ptr].Level > curr.Level{
			result = append(result, curr.Node.Val)
		}
		if curr.Node.Left != nil{
			queue = append(queue, &Entry{Node: curr.Node.Left, Level: curr.Level + 1})
		}
		if curr.Node.Right != nil{
			queue = append(queue, &Entry{Node: curr.Node.Right, Level: curr.Level + 1})
		}
	}

	return result

    
}
// @lc code=end


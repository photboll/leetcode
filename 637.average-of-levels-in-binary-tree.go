package leetcode
/*
 * @lc app=leetcode id=637 lang=golang
 *
 * [637] Average of Levels in Binary Tree
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
func averageOfLevels(root *TreeNode) []float64 {
	levelSum := []int{0}
	levelCount := []int{0}
	queue := make([]*Entry, 1)
	queue[0] = &Entry{Node: root, Level: 0}
	for ptr := 0; ptr < len(queue); ptr++{
		curr := queue[ptr]
		if curr.Node == nil{
			continue
		}
		if curr.Level >= len(levelCount){
			levelCount = append(levelCount, 0)
			levelSum = append(levelSum, 0)
		}

		//process current node 
		levelCount[curr.Level]++
		levelSum[curr.Level] += curr.Node.Val
		//add children to queue
		queue = append(queue, &Entry{Node: curr.Node.Left, Level: curr.Level +1})
		queue = append(queue, &Entry{Node: curr.Node.Right, Level: curr.Level +1})
	}
	result := make([]float64, len(levelCount))
	for i:= range levelCount{
		result[i] = float64(levelSum[i]) / float64(levelCount[i])
	}
	return result
}

// @lc code=end


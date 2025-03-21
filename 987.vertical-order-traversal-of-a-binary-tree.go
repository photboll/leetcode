package leetcode

import (
	"sort"
)

/*
 * @lc app=leetcode id=987 lang=golang
 *
 * [987] Vertical Order Traversal of a Binary Tree
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

func verticalTraversal(root *TreeNode) [][]int {
	if root == nil{
		return nil
	}
	//needs to be map, since keys can be negative 
	crToNodes := map[int]map[int][]*TreeNode{}
	queue := []*TreeNode{root}
	cols := map[*TreeNode]int{}
	rows := map[*TreeNode]int{}
	cols[root] = 0
	rows[root] = 0

	for len(queue) > 0{
		curr := queue[0]//dequeue
		queue = queue[1:]
		// Ensure nested map exists
		if _, exists := crToNodes[cols[curr]]; !exists {
			crToNodes[cols[curr]] = map[int][]*TreeNode{} // Initialize second-level map
		}
		crToNodes[cols[curr]][rows[curr]] = append(crToNodes[cols[curr]][rows[curr]], curr)
		if curr.Left != nil{
			queue = append(queue, curr.Left)
			cols[curr.Left] = cols[curr] -1
			rows[curr.Left] = rows[curr] + 1
		}
		if curr.Right != nil{
			queue = append(queue, curr.Right)
			cols[curr.Right] = cols[curr] + 1
			rows[curr.Right] = rows[curr] + 1
		}
	}

	RowColToSlice:= func ()[][]int{
		var res [][]int
		sortedCols := SortedKeys(crToNodes)
		for _, col:= range sortedCols{
			curColVals := []int{}
			for _, row:= range SortedKeys(crToNodes[col]){
				nodes := crToNodes[col][row]
				sort.Slice(nodes, func (i, j int) bool {
					return nodes[i].Val < nodes[j].Val
				})
				for _, node:= range nodes{
					curColVals = append(curColVals, node.Val)
				}
			}
			res = append(res,  curColVals)
		}
		return res
	}


	return RowColToSlice()
}
func SortedKeys[V any](m map[int]V) []int{
	keys := make([]int, 0, len(m))
	for k := range m{
		keys = append(keys, k)
	}

	sort.Ints(keys)
	return keys
}

// @lc code=end


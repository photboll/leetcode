package leetcode

/*
 * @lc app=leetcode id=101 lang=golang
 *
 * [101] Symmetric Tree
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
func isSymmetric(root *TreeNode) bool {
   if root == nil{
	  return true
   }


   nodes := []*TreeNode{}
   nodes = append(nodes, root.Left, root.Right)
   i:= 0
   for i+1 < len(nodes){
		left := nodes[i]
		right := nodes[i+1]
		if left == nil && right == nil{
			i += 2
			continue
		}else if (left == nil) || (right== nil) || left.Val != right.Val {
			return false
		}

		nodes = append(nodes, left.Left, right.Right)
		nodes = append(nodes, left.Right, right.Left)
		i += 2
   }

   return true
}
// @lc code=end


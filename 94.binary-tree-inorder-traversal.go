/*
 * @lc app=leetcode id=94 lang=golang
 *
 * [94] Binary Tree Inorder Traversal
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

func inorderTraversal(root *TreeNode) []int {
	result := []int{}
	curr := root
	for curr != nil{
		if curr.Left == nil{
			//Current have no left child
			//Append current value and continue with right child
			result = append(result, curr.Val)
			curr = curr.Right
		}else {
			//Find inorder predecessor of curr
			prev :=curr.Left
			for prev.Right != nil && prev.Right != curr{
				prev = prev.Right
			}
			//make curr the right child of its inorder predecessor
			if prev.Right == nil{
				prev.Right = curr
				curr = curr.Left
			}else{
				//revert the chhanges med in the tree
				prev.Right = nil
				result = append(result, curr.Val)
				curr = curr.Right
			}
		}
	}
	return result
}
func inorderTraversalRecursive(root *TreeNode) []int {
   if root == nil{
	return nil
   }
   result := []int{}
   result = append(result, inorderTraversal(root.Left)...)
   result = append(result, root.Val)
   result = append(result, inorderTraversal(root.Right)...)
   return result
}
// @lc code=end


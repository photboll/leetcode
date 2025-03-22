package leetcode
/*
 * @lc app=leetcode id=138 lang=golang
 *
 * [138] Copy List with Random Pointer
 */

// @lc code=start
/**
 * Definition for a Node.
 * type Node struct {
 *     Val int
 *     Next *Node
 *     Random *Node
 * }
 */

func copyRandomList(head *Node) *Node {
	//Start with creating a copys of each individual node in a map 
	cop := map[*Node]*Node{}//Maps Node : CopiedNode
	curr := head
	for curr!= nil{//Init all node copies, let their pointers be nil
		cop[curr] = &Node{Val: curr.Val}
		curr = curr.Next
	}

	//traverse the list once more but now setting the copys pointers
	curr = head
	for curr != nil{
		cop[curr].Next = cop[curr.Next]
		cop[curr].Random = cop[curr.Random]
		curr = curr.Next
	}

	return cop[head]
}
// @lc code=end


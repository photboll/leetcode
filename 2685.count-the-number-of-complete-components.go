package leetcode

import "fmt"

/*
 * @lc app=leetcode id=2685 lang=golang
 *
 * [2685] Count the Number of Complete Components
 */

// @lc code=start
func countCompleteComponents(n int, edges [][]int) int {
	edgeMap := map[int][]int{} 
	for _, e := range edges{
		edgeMap[e[0]] = append(edgeMap[e[0]], e[1])
		edgeMap[e[1]] = append(edgeMap[e[1]], e[0])
	}
	count := 0
	visited := make([]bool, n)//Have we visited[node] before?
	//The idea is to DFS thorugh each subgraph and count the edges and nodes within
	for start := 0; start < n; start++{//outer loop to makes sure we process all subgraphs 
		if visited[start]{
			continue
		}
		//start dfs from start node 
		visited[start] = true
		edgeCount := 0//Actually counts directed edges, so it will be doubled
		nodeCount := 0
		stack := []int{start}
		for len(stack)> 0{
			curr := stack[len(stack)-1]//Pop from the stack
			stack = stack[:len(stack)-1]

			nodeCount++
			edgeCount += len(edgeMap[curr])//This should return empyt slices for nodes with no edges
			for _, next := range edgeMap[curr]{
				if !visited[next]{
					stack = append(stack, next)
					visited[next] = true//Mark next as visited
				}
			}
		}
		//A complete component most have 2*|E| = |V| * (|V|-1)
		if edgeCount== nodeCount *(nodeCount -1){
			count++
		}
	}
	return count
}
// @lc code=end


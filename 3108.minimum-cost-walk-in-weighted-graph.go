package leetcode

import "math"

/*
 * @lc app=leetcode id=3108 lang=golang
 *
 * [3108] Minimum Cost Walk in Weighted Graph
 */

// @lc code=start
type UnionFindAnd struct{
	Rank, Parent, MinCost []int//MinCost will the minimum cost walk for a completed component	
}

func NewUnionFindAnd(size int) *UnionFindAnd{
	minCost := make([]int, size)
	for i := range minCost{
		minCost[i] = math.MaxInt
	}
	parents := make([]int, size)
	for i := range parents{
		parents[i] =i// Init every element is its on parent,
		//Which means that that every node is in its own disjoint set
	}
	return &UnionFindAnd{
		Rank: make([]int, size),
		Parent: parents,  
		MinCost: minCost,
	}
}

// Find the representative of the set that vertice v belongs to
func (ufa *UnionFindAnd) Find(v int) int{
	repr := ufa.Parent[v]
	//Is repr the actual representative of the group 
	if ufa.Parent[repr] != ufa.Parent[v] {
		//Find the representative of this set by recurisvely call it till we get the root
		ufa.Parent[v] = ufa.Find(repr)
	}
	return ufa.Parent[v]
}

//Union the sets of v and u, rember to update min cost based on the edges weight
func (ufa *UnionFindAnd) Union(v, u, weight int){
	vRepr := ufa.Find(v)
	uRepr := ufa.Find(u)
	
	//check if they are in the same set/component
	if vRepr == uRepr{
		//This edge can make the minuimum cost even smaller 
		//We use bitwise AND zero out more bits in minCost
		ufa.MinCost[vRepr] &= weight
		return
	}

	//Union by Rank, the representative with the highest rank should remain the representative of the union
	if ufa.Rank[vRepr] < ufa.Rank[uRepr]{
		ufa.Parent[vRepr] = uRepr
		ufa.MinCost[uRepr] &= weight & ufa.MinCost[vRepr]
	} else if ufa.Rank[uRepr] < ufa.Rank[vRepr] {
		ufa.Parent[uRepr] = vRepr
		ufa.MinCost[vRepr] &= weight & ufa.MinCost[uRepr]
	} else {
		ufa.Parent[uRepr] = vRepr
		ufa.Rank[vRepr]++
		ufa.MinCost[vRepr] &= weight & ufa.MinCost[uRepr]
	}
	ufa.MinCost[ufa.Find(v)] &= weight
}

//Query returns the minimum cost if u and v belong to the same connected component else -1
func (ufa *UnionFindAnd) Query(s, t int) int {
	sRepr := ufa.Find(s)
	tRepr := ufa.Find(t)
	//They belong to the same component
	if sRepr == tRepr{
		return ufa.MinCost[sRepr]
	}
	return -1

}

func minimumCost(n int, edges [][]int, query [][]int) []int {
    result := make([]int, len(query))
	ufa := NewUnionFindAnd(n)
	for i := range edges{
		ufa.Union(edges[i][0], edges[i][1], edges[i][2])
	}
	
	for i:= range query{
		result[i]= ufa.Query(query[i][0], query[i][1])
	}
	return result
}
// @lc code=end


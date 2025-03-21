package leetcode

import (
	"sort"
)

/*
 * @lc app=leetcode id=274 lang=golang
 *
 * [274] H-Index
 */

// @lc code=start
func hIndex(citations []int) int {
	sort.Slice(citations, func(i, j int) bool {
		return citations[i] > citations[j]
	})
	h := 0
	for i:= 0; i < len(citations); i++{
		if citations[i] >= i + 1{ 
			h = i+1
		}else{
			break
		}
	}
	return h
}
// @lc code=end


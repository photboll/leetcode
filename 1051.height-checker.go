package leetcode

import "sort"

/*
 * @lc app=leetcode id=1051 lang=golang
 *
 * [1051] Height Checker
 */

// @lc code=start
func heightChecker(heights []int) int {
	expected := make([]int, len(heights))
	copy(expected, heights)
    sort.Slice(expected, func(i, j int) bool{
		return expected[i] < expected[j]
	})
	cntOutOfOrder := 0
	for i:= 0; i < len(heights); i++{
		if heights[i] != expected[i]{
			cntOutOfOrder++
		}
	}
	return cntOutOfOrder
}
// @lc code=end


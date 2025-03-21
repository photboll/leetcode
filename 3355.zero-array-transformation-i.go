package leetcode

/*
 * @lc app=leetcode id=3355 lang=golang
 *
 * [3355] Zero Array Transformation I
 */

// @lc code=start

func isZeroArray(nums []int, queries [][]int) bool {
	diff := make([]int, len(nums)+1)
	for _, query := range queries {
		diff[query[0]]++
		diff[query[1]+1]--
	}
	for i := 1; i < len(diff); i++ {
		diff[i] += diff[i-1]
	}

	for i, num := range nums {
		if diff[i] < num {
			return false
		}
	}
	return true
}

// @lc code=end

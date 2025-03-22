package leetcode

/*
 * @lc app=leetcode id=217 lang=golang
 *
 * [217] Contains Duplicate
 */

// @lc code=start
func containsDuplicate(nums []int) bool {
	set := map[int]struct{}{}
	for _, num := range nums {
		set[num] = struct{}{}
	}
	return len(set) != len(nums)
}

// @lc code=end

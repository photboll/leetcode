/*
 * @lc app=leetcode id=57 lang=golang
 *
 * [57] Insert Interval
 */

// @lc code=start

func insert(intervals [][]int, newInterval []int) [][]int {
	result := [][]int{}
	i := 0
	n := len(intervals)

	// Add all intervals before newInterval (non-overlapping)
	for i < n && intervals[i][1] < newInterval[0] {
		result = append(result, intervals[i])
		i++
	}

	// Merge overlapping intervals
	for i < n && intervals[i][0] <= newInterval[1] {
		newInterval[0] = min(newInterval[0], intervals[i][0])
		newInterval[1] = max(newInterval[1], intervals[i][1])
		i++
	}
	result = append(result, newInterval)

	// Add remaining intervals
	for i < n {
		result = append(result, intervals[i])
		i++
	}

	return result
}
// @lc code=end


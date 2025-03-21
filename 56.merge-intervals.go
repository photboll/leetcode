package leetcode

import "sort"

/*
 * @lc app=leetcode id=56 lang=golang
 *
 * [56] Merge Intervals
 */

// @lc code=start
func merge(intervals [][]int) [][]int {
	sort.SliceStable(intervals, func(i, j int) bool {
		return intervals[i][0] < intervals[j][0]
	})
	cntMergedIntervals := 0
	for i := 1; i < len(intervals); i++{
		if intervals[i][0] <= intervals[cntMergedIntervals][1]{
			//current start is earlier than previous end i.e. they overlap
			//adjust the earlier intervals endtime to include current endtime
			intervals[cntMergedIntervals][1] = max(intervals[i][1], intervals[cntMergedIntervals][1]) 
		} else {
			//add it to the merged intervals slice
			cntMergedIntervals++
			intervals[cntMergedIntervals] = intervals[i]
		}
	}

	return intervals[:cntMergedIntervals+1]
}
// @lc code=end


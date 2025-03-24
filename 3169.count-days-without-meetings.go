package leetcode
import "sort"
/*
 * @lc app=leetcode id=3169 lang=golang
 *
 * [3169] Count Days Without Meetings
 */

// @lc code=start
func countDays(days int, meetings [][]int) int {
    sort.Slice(meetings, func (i, j int) bool {
		return meetings[i][0]< meetings[j][0]
	})
	countNonOverlapping := 0
	//Merge overlapping intervals 
	for i:= 1 ; i< len(meetings); i++{
		//The end of the previous meetings is later than the current start
		if  meetings[i][0] <= meetings[countNonOverlapping][1] {
			//The new end time will be whichever is later
			meetings[countNonOverlapping][1] = max(meetings[countNonOverlapping][1], meetings[i][1])
		}else {
			countNonOverlapping++
			meetings[countNonOverlapping] = meetings[i]
		}
	}
	//Remove the tail of meetings whit the old overlapped intervals 
	countNonOverlapping++
	meetings = meetings[:countNonOverlapping]
	//count number of days missing in meetings
	daysAvailable := meetings[0][0] -1//all days before the first meetings is available 
	for i:= 1; i< countNonOverlapping ; i++{
		daysAvailable += max(meetings[i][0] - meetings[i-1][1] -1, 0)
	}
	//check if their are any days available after the last meeting 
	daysAvailable += days - meetings[len(meetings) - 1][1]
	return daysAvailable
}
// @lc code=end


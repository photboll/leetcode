package leetcode
/*
 * @lc app=leetcode id=3356 lang=golang
 *
 * [3356] Zero Array Transformation II
 */

// @lc code=start
func minZeroArray(nums []int, queries [][]int) int {
	n := len(nums); sum := 0; k:= 0
	diff := make([]int, n+ 1)
	for i:=0; i < n ; i++{
		for sum + diff[i] < nums[i]{
			//Expand the number of queries used
			if k == len(queries) {
				return -1
			}
			l := queries[k][0]
			r := queries[k][1]
			val := queries[k][2]
			k++

			//mark beginning and end in the difference array
			if r< i {continue}//important since if r is less than i than this query has no effect on diff at all,
			diff[max(l, i)] += val 
			diff[r+1] -= val
		}
		sum += diff[i]
	}
	return k
}
// @lc code=end


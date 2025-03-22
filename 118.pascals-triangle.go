package leetcode
/*
 * @lc app=leetcode id=118 lang=golang
 *
 * [118] Pascal's Triangle
 */

// @lc code=start
func generate(numRows int) [][]int {
	result := [][]int{[]int{1}}
 	for i := 0; i+1<numRows; i++{
		row := []int{1}
		for j:= 0; j+1< len(result[i]); j++{
			row = append(row, result[i][j] + result[i][j+1])
		}
		row = append(row, 1)
		result = append(result, row)
	}
	return result
}
// @lc code=end


/*
 * @lc app=leetcode id=766 lang=golang
 *
 * [766] Toeplitz Matrix
 */

// @lc code=start
func isToeplitzMatrix(matrix [][]int) bool {
	//Divide the problem into two parts
	//1. check all diagonals starting in the first column
	//2. Check all diagonal  starting in the first row
	m := len(matrix); n := len(matrix[0])
	
	for r:= 0;r + 1 < m; r++{
		for c:= 0; c +1< n; c++{
			if matrix[r][c] != matrix[r+1][c+1]{
				return false
			}
		}
	} 
	return true
    
}
// @lc code=end


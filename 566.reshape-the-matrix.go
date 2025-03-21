package leetcode

import "fmt"

/*
 * @lc app=leetcode id=566 lang=golang
 *
 * [566] Reshape the Matrix
 */

// @lc code=start
func matrixReshape(mat [][]int, r int, c int) [][]int {
    m := len(mat); n := len(mat[0])
	if n*m != r*c{
		//Invalid target shape, 
		return mat
	}

	result := make([][]int, r)
	for i := range result{
		result[i] = make([]int, c)
	}

	for i:= range mat{
		for j:= range mat[i]{
			number := i*n + j
			newI := number / c
			newJ := number % c
			result[newI][newJ] = mat[i][j]
		}
	
	}
	return result
}
// @lc code=end


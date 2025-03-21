package leetcode

import "fmt"

/*
 * @lc app=leetcode id=498 lang=golang
 *
 * [498] Diagonal Traverse
 */

// @lc code=start
type Direction int
const (
	Up Direction = iota 
	Down 
)

func findDiagonalOrder(mat [][]int) []int {
	m := len(mat); n := len(mat[0])
	result := make([]int, m*n)
	i := 0; j := 0; curDir := Up
	NextPosition := func(i, j int, curDir Direction) (int, int, Direction){
		switch curDir{
		case Up:
			if  j == n -1 {
				//At the right edge 
				return i+1, j, Down 
			} else if i == 0{
				//At the top edge
				return i, j+1, Down
			} else{
				//Anywhere else contine in the same direction
				return i - 1, j+1, Up
			}

		case Down:
			if i == m - 1{
				//At the Bottom edge
				return i, j+1, Up
			} else if j == 0 {
				//At the left edge
				return i+1, j, Up
			} else {
				//Continue on Down to the left 
				return i + 1, j - 1, Down
			}
		}
		panic("invalid direction")
	}
	for pos :=0 ; pos < m*n; pos++{
		result[pos] = mat[i][j]
		i, j, curDir = NextPosition(i, j, curDir)
	}

	return result
}
// @lc code=end


package leetcode
/*
 * @lc app=leetcode id=201 lang=golang
 *
 * [201] Bitwise AND of Numbers Range
 */

// @lc code=start
func rangeBitwiseAnd(left int, right int) int {
	countZeros := 0
	for left != right {
		left = left >> 1
		right = right >> 1
		countZeros++
	}
	return left << countZeros
}
// @lc code=end


package leetcode
/*
 * @lc app=leetcode id=191 lang=golang
 *
 * [191] Number of 1 Bits
 */

// @lc code=start
func hammingWeight(n int) int {
    tot := 0
	for n != 0{
		tot += (n & 1)
		n = n >> 1
	}
	return tot
}
// @lc code=end


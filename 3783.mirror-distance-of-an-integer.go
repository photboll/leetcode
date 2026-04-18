/*
 * @lc app=leetcode id=3783 lang=golang
 *
 * [3783] Mirror Distance of an Integer
 */

// @lc code=start
func reverse(num int) int{
	res := 0

	for num > 0 {
		rem := num % 10
		res = 10*res + rem
		num /= 10
	}
	return res

}
func abs(x int) int{
	mask := x >> 63
	return (x ^ mask) - mask
}
func mirrorDistance(n int) int {
	return abs(n - reverse(n))
}
// @lc code=end


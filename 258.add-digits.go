package leetcode
/*
 * @lc app=leetcode id=258 lang=golang
 *
 * [258] Add Digits
 */

// @lc code=start
func addDigits(num int) int {
   	for num > 9{
		x := 0
		for num > 0{
			x += num % 10
			num /= 10
	}
		num = x
   } 
   return num
}
// @lc code=end


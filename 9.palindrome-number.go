package leetcode
import "strconv"
/*
 * @lc app=leetcode id=9 lang=golang
 *
 * [9] Palindrome Number
 */

// @lc code=start
func isPalindrome(x int) bool {
    runes := []rune(strconv.Itoa(x)) 
	n := len(runes)
	for i:=0; i<n/2;i++{
		if runes[i] != runes[n-i-1]{
			return false
		}
	}
	return true
}
// @lc code=end
/*
 * @lc app=leetcode id=3191 lang=golang
 *
 * [3191] Minimum Operations to Make Binary Array Elements Equal to One I
 */

// @lc code=start
func minOperations(nums []int) int {
	numOperations := 0
	n:= len(nums)
	for i:= range nums[:n - 2]{
		if nums[i] == 0 {
			numOperations++
			for j:= i; j< i+3; j++{
				switch nums[j] {
				case 0:
					nums[j] = 1
				case 1:
					nums[j] = 0
				}
			}
		}
	}
	
	if nums[n - 1] == 0 || nums[n-2] == 0{
		return -1
	}
	return numOperations
}
// @lc code=end


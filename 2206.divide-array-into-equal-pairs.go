/*
 * @lc app=leetcode id=2206 lang=golang
 *
 * [2206] Divide Array Into Equal Pairs
 */

// @lc code=start
func divideArray(nums []int) bool {
   counts := make([]int, 500) 
   for _, num := range nums{
	counts[num-1]++
   }
   for _, count := range counts{
	if count % 2 == 1{
		return false
	}
   }
   return true
}
// @lc code=end


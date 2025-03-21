package leetcode
/*
 * @lc app=leetcode id=2401 lang=golang
 *
 * [2401] Longest Nice Subarray
 */

// @lc code=start
func longestNiceSubarray(nums []int) int {
	l := 0
	maxWindowSize := 1
	x := nums[l] //Tracks whihc bits are set in the current window
	for r:= 1 ; r < len(nums); r++{
		for l < len(nums) && nums[r] & x != 0{
			//Reset the current window to start here instead 
			// or do I need to know which number made it not Nice?
			// But I don't keep that information in x,  maybe I need to make it a prefix-like array instead
			// No, since we always make sure that they are no conlficts when adding,
			//There will never be two numbers which causes a subarray to be not nice. 
			// Otherwise those two numbers would have cause it to be not nice
			//So we can simply remove numbers from the left, until the condition is true again
		
			x ^= nums[l]
			l++
		}

		//Can we add the current number to the subarray and keep it Nice
		if nums[r]  & x == 0{
			//It will still be nice
			if r - l + 1> maxWindowSize{
				maxWindowSize = r - l + 1
			}
			//add the current number to x
			x ^= nums[r]
		} 

		
			
	}
	return maxWindowSize
}
// @lc code=end


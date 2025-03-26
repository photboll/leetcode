package leetcode

import "math/rand"

/*
 * @lc app=leetcode id=215 lang=golang
 *
 * [215] Kth Largest Element in an Array
 */

// @lc code=start
func findKthLargest(nums []int, k int) int {
    return quickselect(nums, k)
}
func quickselect(nums []int, k int) int {
	n := len(nums)
	start:= 0
	end := n -1
	for start < end {
		i := partition(nums, start, end )
		if i == n -k{
			return nums[i]
		} else if i < n-k{
			start = i+1
		}else{
			end = i-1
		}
	}
	return nums[start]
}
func partition(nums []int, start, end int)int {
	pivot := rand.Intn(end - start) + start 
	swap(nums, pivot, end )

	left := start
	for curr:= start; curr < end; curr ++{
			if nums[curr] < nums[end]{
				//current is smaller than the pivot 
				swap(nums, left, curr)
				left++
			}
	}
	swap(nums, left, end)//Put the pivot back in its correct position
	return left
}
func swap(nums []int, i, j int){
	nums[i], nums[j] = nums[j], nums[i]
}
// @lc code=end


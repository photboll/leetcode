package leetcode

import "strconv"

/*
 * @lc app=leetcode id=190 lang=golang
 *
 * [190] Reverse Bits
 */

// @lc code=start
func reverseBits(num uint32) uint32 {
	var res uint32
	for i := 0; i < 32; i++{
		res = res << 1 //Move over the result one bit 
		res |= (num & 1)//Add the first bit of num to result
		num = num >> 1 //Move the num to get to the next bit
	}
	return res
}
// @lc code=end


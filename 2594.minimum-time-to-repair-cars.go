package leetcode

import (
	"math"
)

/*
 * @lc app=leetcode id=2594 lang=golang
 *
 * [2594] Minimum Time to Repair Cars
 */

// @lc code=start
func countRepairedCars(ranks []int, time int64) int64{
	var repairedCars int64
	for _, rank:= range ranks{
		repairedCars += int64(math.Floor(math.Sqrt(float64(time/ int64(rank)))))
	}
	return repairedCars
}
func repairCars(ranks []int, cars int) int64 {
	low := int64(1)
	high := int64(math.MaxInt64)
	for low <= high{
		mid := low + (high - low)/2

		if countRepairedCars(ranks, mid) >= int64(cars){
			//We might be able to do with less time
			high = mid - 1
		}else {
			low = mid + 1
		}
	}
	return low 
}
// @lc code=end


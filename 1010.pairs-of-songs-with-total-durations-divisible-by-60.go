package leetcode
/*
 * @lc app=leetcode id=1010 lang=golang
 *
 * [1010] Pairs of Songs With Total Durations Divisible by 60
 */

// @lc code=start
func numPairsDivisibleBy60(time []int) int {
	count := 0
	remCounts := make([]int, 60)
	for _, t := range time{
		rem := t % 60
		complement := (60 - rem) % 60
		count += remCounts[complement]
		remCounts[rem]++
		//fmt.Println(count, rem, complement, remCounts)
	}
	return count
    
}
// @lc code=end


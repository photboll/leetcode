/*
 * @lc app=leetcode id=135 lang=golang
 *
 * [135] Candy
 */

// @lc code=start
func Sum(nums []int) int{
    sum  := 0
    for _, num := range nums{
        sum += num
    }
    return sum
}

func candy(ratings []int) int {
    /*
    AZt minimum there wil be len(ratings) candies given out at all times
    THeere seems to be a sort of localityl lto the problem. the actual value of the rating does not matter.
    only its relation to its immediate neighbors. 

    If a persons rating is lower than both of its neighbors  then they will always be given a single candy
    this could be used to break up the whole problem into subproblems.
    */

    candies := make([]int, len(ratings))
    candies[0] = 1
    //first pass left to right 
    for i:= 1; i < len(ratings); i++{
        if ratings[i] > ratings[i-1]{
            //if cur childs rating is larger than its left side neighbor then it should be given one more 
            candies[i] = candies[i-1] + 1
        } else {
            //otherwise they will only get one candy
            candies[i] = 1
        }
    }

    for i:= len(ratings) -2; i > -1; i--{
        if ratings[i] > ratings[i+1] && candies[i] <= candies[i+1]{
            //if cur child have a higher rating than RH neighbnor and less or equal candies, we neew to adjust
            candies[i] = candies[i+1] +1
        }
    }

    return Sum(candies)
}
// @lc code=end


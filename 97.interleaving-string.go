package leetcode	
/*
 * @lc app=leetcode id=97 lang=golang
 *
 * [97] Interleaving String
 */

// @lc code=start
func isInterleave(s1 string, s2 string, s3 string) bool {
	r1 := []rune(s1)
	r2 := []rune(s2)
	r3 := []rune(s3)
	if len(r1) + len(r2) != len(r3){
		return false
	}
	dp := make([][]bool, len(r1)+1)
	for i := range dp{
		dp[i] = make([]bool, len(r2)+1)
	}

	//Init dp 
	dp[0][0] = true //Empty strings can always be interlevaed into another empty string 
	for j := 1; j < len(dp[0]);j++{
		dp[0][j] = dp[0][j-1] && r2[j-1] == r3[j-1]
	}
	for i := 1; i < len(dp);i++{
		dp[i][0] = dp[i-1][0] && r1[i-1] == r3[i-1]
	}

	for i:= 1; i< len(dp); i++{
		for j:= 1; j<len(dp[0]);j++{
			if (r1[i-1] == r3[i+j-1] && dp[i-1][j]) || (r2[j-1] == r3[i+j-1] && dp[i][j-1]){
				dp[i][j] = true
			}
		}
	}

	return dp[len(r1)][len(r2)]
}
// @lc code=end


package leetcode

import "strings"

/*
 * @lc app=leetcode id=290 lang=golang
 *
 * [290] Word Pattern
 */

// @lc code=start
func wordPattern(pattern string, s string) bool {
    cToW := map[rune]string{} //Char to word, the mapping from each char in pattern to eachword in s
	wToC := map[string]rune{}
	words := strings.Fields(s)
	if len(words) != len(pattern) {
		return false
	}
	for i, char := range pattern{
		w, exists := cToW[char]
		if exists && words[i] != w{
			return false
		}else {
			cToW[char] = words[i]
		}
		//Check if duplicate mapping 
		c, exists := wToC[words[i]]
		if exists && c != char{
			return false
		}else{
			wToC[words[i]] = char
		}

	}


	return true
}
// @lc code=end


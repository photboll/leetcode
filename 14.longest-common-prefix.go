package leetcode

import "strings"

/*
 * @lc app=leetcode id=14 lang=golang
 *
 * [14] Longest Common Prefix
 */

// @lc code=start
func longestCommonPrefix(strs []string) string {
	if len(strs) == 0{
		return ""
	}

	prefix := strs[0]
	for _, word := range strs[1:]{
		for strings.Index(word, prefix) != 0{
			//as long as the prefix is does not math the first part of word 
			//try to make the prefix shorter
			prefix = prefix[:len(prefix)-1]
			if prefix == ""{
				return ""
			}
		}
	}

	return prefix 
}
// @lc code=end


package leetcode

import "sort"

/*
 * @lc app=leetcode id=49 lang=golang
 *
 * [49] Group Anagrams
 */

// @lc code=start
func getAllValues(dict map[string][]string) [][]string {
	values := [][]string{}
	for _, v := range dict {
		values = append(values, v)
	}
	return values
}
func groupAnagrams(strs []string) [][]string {
	groups := make(map[string][]string)

	for _, str := range strs {
		runes := []rune(str)
		sort.Slice(runes, func(i, j int) bool {
			return runes[i] < runes[j]
		})
		sort_str := string(runes)
		groups[sort_str] = append(groups[sort_str], str)
	}
	return getAllValues(groups)
}

// @lc code=end

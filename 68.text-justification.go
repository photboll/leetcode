package leetcode

import "strings"

/*
 * @lc app=leetcode id=68 lang=golang
 *
 * [68] Text Justification
 */

// @lc code=start
func FullJustifyLine(words [][]rune, width, lineLen int) string {
	spaces := width - lineLen
	numGaps := len(words) - 1
	if numGaps == 0{
		return LeftJustifyLine(words, width)
	}
	gapsWithExtra := spaces % numGaps
	smallGap := strings.Repeat(" ", spaces/numGaps + 1)
	sb := strings.Builder{}
	for i, runes := range words {
		sb.WriteString(string(runes))
		if i < numGaps {
			sb.WriteString(smallGap)
			if i < gapsWithExtra {
				sb.WriteString(" ")
			}
		}
	}
	return sb.String()
}
func LeftJustifyLine(words [][]rune, width int) string {
	sb := strings.Builder{}
	n := len(words)
	for i, runes := range words {
		sb.WriteString(string(runes))
		if i+1 < n {
			sb.WriteString(" ")
		}
	}
	sb.WriteString(strings.Repeat(" ", width - sb.Len()))
	return sb.String()

}
func stringsToRunes(words []string) [][]rune {
	result := make([][]rune, len(words))
	for i, word := range words {
		result[i] =  []rune(word)
	}
	return result
}
func fullJustify(words []string, maxWidth int) []string {
	wordRunes := stringsToRunes(words)
	result := []string{}
	i := 0
	n := len(words)
	for i < n {
		lineLen := len(wordRunes[i])
		j := i + 1

		//How many words fit on this line
		for j < n && lineLen+1+len(wordRunes[j]) <= maxWidth {
			lineLen += 1 + len(wordRunes[j])
			j++
		}
		//the final line and one word lines should be left justified
		if j == n || j-i == 1 {
			result = append(result, LeftJustifyLine(wordRunes[i:j], maxWidth))
		} else {
			//All other lines should be fully_justified
			result = append(result, FullJustifyLine(wordRunes[i:j], maxWidth, lineLen))
		}
		//Move onto the next line
		i = j

	}
	return result
}

// @lc code=end

package leetcode

import (
	"strings"
)

/*
 * @lc app=leetcode id=415 lang=golang
 *
 * [415] Add Strings
 */

// @lc code=start

func charToInt(c byte) int {
	return int(c - '0')
}

func addDigits(d1, d2 byte, carry int) (int, int) {
	sum := charToInt(d1) + charToInt(d2) + carry
	return sum % 10, sum / 10
}

func addStrings(num1, num2 string) string {
	var sb strings.Builder
	if len(num1) < len(num2) {
		num1, num2 = num2, num1 // Ensure num1 is the longer number
	}

	n1, n2 := len(num1), len(num2)
	carry := 0

	for i := 0; i < n1 || carry > 0; i++ {
		d1 := byte('0')
		if i < n1 {
			d1 = num1[n1-1-i]
		}

		d2 := byte('0')
		if i < n2 {
			d2 = num2[n2-1-i]
		}

		rem, newCarry := addDigits(d1, d2, carry)
		sb.WriteByte(byte('0' + rem))
		carry = newCarry
	}

	// Reverse the string and return
	result := []byte(sb.String())
	for i, j := 0, len(result)-1; i < j; i, j = i+1, j-1 {
		result[i], result[j] = result[j], result[i]
	}
	return string(result)
}

// @lc code=end


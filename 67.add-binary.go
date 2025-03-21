package leetcode

/*
 * @lc app=leetcode id=67 lang=golang
 *
 * [67] Add Binary
 */

// @lc code=start

func addBits(a, b, c byte) (byte, byte) {
    numSet := 0
    if a == '1' {
        numSet++
    }
    if b == '1' {
        numSet++
    }
    if c == '1' {
        numSet++
    }

    switch numSet {
    case 3:
        return '1', '1' // Carry '1', current bit '1'
    case 2:
        return '1', '0' // Carry '1', current bit '0'
    case 1:
        return '0', '1' // Carry '0', current bit '1'
    default:
        return '0', '0' // Carry '0', current bit '0'
    }
}

func addBinary(a string, b string) string {
    carry := byte('0')
    var curBit byte
    maxLen := len(a)
    if len(b) > maxLen {
        maxLen = len(b)
    }

    // Ensure both strings are of equal length by padding the shorter one with '0's
    result := make([]byte, maxLen+1)

    // Loop through both strings from right to left
    for i := 0; i < maxLen; i++ {
        bita := byte('0')
        bitb := byte('0')

        if i < len(a) {
            bita = a[len(a)-1-i]
        }
        if i < len(b) {
            bitb = b[len(b)-1-i]
        }

        carry, curBit = addBits(bita, bitb, carry)
        result[maxLen-i] = curBit
    }

    // Handle final carry if present
    if carry == '1' {
        result[0] = carry
        return string(result)
    } else {
        // Return the result without the leading zero
        return string(result[1:])
    }
}

// @lc code=end


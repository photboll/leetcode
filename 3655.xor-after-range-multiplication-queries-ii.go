/*
 * @lc app=leetcode id=3655 lang=golang
 *
 * [3655] XOR After Range Multiplication Queries II
 */

// @lc code=start
package main

import (
	"fmt"
)

func xorAfterQueries(nums []int, queries [][]int) int {
	const MOD = 1000000007
	n := len(nums)
	
	// Square root threshold
	B := 316

	// Work with int64 to prevent overflow during intermediate multiplications
	nums64 := make([]int64, n)
	for i, v := range nums {
		nums64[i] = int64(v)
	}

	type qryInfo struct {
		l, r, v int
	}
	smallK := make([][]qryInfo, B)

	// Process queries and bucket by step size k
	for _, qry := range queries {
		l, r, k, v := qry[0], qry[1], qry[2], qry[3]
		if v == 1 {
			continue // Multiplier 1 changes nothing
		}
		if k >= B {
			// Case 1: Large k - process directly
			v64 := int64(v)
			for i := l; i <= r; i += k {
				nums64[i] = (nums64[i] * v64) % MOD
			}
		} else {
			// Case 2: Small k - store for batch processing
			smallK[k] = append(smallK[k], qryInfo{l, r, v})
		}
	}

	// Precompute modular inverses for v up to 10^5
	invs := make([]int64, 100001)
	invs[1] = 1
	for i := 2; i <= 100000; i++ {
		invs[i] = (int64(MOD) - (int64(MOD/i)*invs[MOD%i])%int64(MOD)) % int64(MOD)
	}

	// diff array for range-multiplication tracking
	diff := make([]int64, n+B+1)
	for i := range diff {
		diff[i] = 1
	}

	// Batch process small k
	for k := 1; k < B; k++ {
		if len(smallK[k]) == 0 {
			continue
		}
		
		// Apply queries to diff array
		for _, q := range smallK[k] {
			l, r, v := q.l, q.r, q.v
			diff[l] = (diff[l] * int64(v)) % MOD
			
			m := (r - l) / k
			lastIdx := l + (m+1)*k
			diff[lastIdx] = (diff[lastIdx] * invs[v]) % MOD
		}

		// Sweep each sub-sequence modulo k
		for r := 0; r < k; r++ {
			curr := int64(1)
			for i := r; i < n; i += k {
				curr = (curr * diff[i]) % MOD
				if curr != 1 {
					nums64[i] = (nums64[i] * curr) % MOD
				}
			}
			// Reset diff array for the next k
			for i := r; i < n+k; i += k {
				diff[i] = 1
			}
		}
	}

	// Calculate XOR of all elements
	var result int64
	for _, v := range nums64 {
		result ^= v
	}
	return int(result)
}
// @lc code=end


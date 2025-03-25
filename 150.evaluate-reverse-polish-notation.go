package leetcode

import (
	"strconv"
)

/*
 * @lc app=leetcode id=150 lang=golang
 *
 * [150] Evaluate Reverse Polish Notation
 */

// @lc code=start
type Stack struct {
	data []int
}

func NewStack() *Stack {
	return &Stack{data: []int{}}
}
func (s *Stack) Push(val int) {
	s.data = append(s.data, val)
}
func (s *Stack) Pop() int {
	lastI := max(len(s.data)-1, 0)
	val := s.data[lastI]
	s.data = s.data[:lastI]
	return val
}

func evalRPN(tokens []string) int {
	var op1, op2 int
	stack := NewStack()
	for _, token := range tokens {
		num, err := strconv.Atoi(token)
		if err != nil {
			op1 = stack.Pop()
			op2 = stack.Pop()
			switch token {
			case "+":
				stack.Push(op1 + op2)
			case "-":
				stack.Push(op2 - op1)
			case "*":
				stack.Push(op2 * op1)
			case "/":
				stack.Push(op2 / op1)
			}
		} else {
			stack.Push(num)
		}
	}
	return stack.Pop()
}

// @lc code=end

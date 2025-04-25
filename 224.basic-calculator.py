#
# @lc app=leetcode id=224 lang=python3
#
# [224] Basic Calculator
#
# https://leetcode.com/problems/basic-calculator/description/
#
# algorithms
# Hard (45.09%)
# Likes:    6595
# Dislikes: 535
# Total Accepted:    579.5K
# Total Submissions: 1.3M
# Testcase Example:  '"1 + 1"'
#
# Given a string s representing a valid expression, implement a basic
# calculator to evaluate it, and return the result of the evaluation.
# 
# Note: You are not allowed to use any built-in function which evaluates
# strings as mathematical expressions, such as eval().
# 
# 
# Example 1:
# 
# 
# Input: s = "1 + 1"
# Output: 2
# 
# 
# Example 2:
# 
# 
# Input: s = " 2-1 + 2 "
# Output: 3
# 
# 
# Example 3:
# 
# 
# Input: s = "(1+(4+5+2)-3)+(6+8)"
# Output: 23
# 
# 
# 
# Constraints:
# 
# 
# 1 <= s.length <= 3 * 10^5
# s consists of digits, '+', '-', '(', ')', and ' '.
# s represents a valid expression.
# '+' is not used as a unary operation (i.e., "+1" and "+(2 + 3)" is
# invalid).
# '-' could be used as a unary operation (i.e., "-1" and "-(2 + 3)" is
# valid).
# There will be no two consecutive operators in the input.
# Every number and running calculation will fit in a signed 32-bit integer.
# 
# 
#

# @lc code=start
OPS = set(["-", "+"])
DIGITS = set([str(i) for i in range(10)])
WHITESPACE = set([" "])
class Parser:
    def parse(self, text):
        self.text = text
        self.pos = -1
        self.len = len(text) 
        return self.start()
    
    def eat_whitespace(self):
        while self.pos < self.len and self.text[self.pos+1] in WHITESPACE:
            self.pos += 1

class CalcParser(Parser):
    def start(self):
        return self.expression()
    
    def expression(self, value=0):
        #Experssion -> Term (("+"|"-") Term)*
        #Expression -> -Expression
        #Expression -> "(" Expression ")"
        value = self.term()
        while self.has_next():
            token = self.peek_next()
            if token == "+":
                self.next()
                value += self.term()
            elif token == "-":
                self.next()
                value -= self.term()
            else:
                break
        return value
                 
    def term(self):
        token = self.peek_next()
        #Unary -
        if token == "-":
            self.next()
            return -self.term()
        elif token == "(":
            self.next()
            value = self.expression()
            if self.peek_next() != ")":
                raise ValueError("Missing Closing parenthesis")
            self.next()
            return value
        else:
            return self.number()
    def number(self) -> int:
        #Number -> -digits* | digits*
        chars = []
        while self.has_next() and self.peek_next().isdigit():
            chars.append(self.next())
            
        print( chars, self.peek_next())
        return int("".join(chars))
        
    def next(self) -> str:
        value = self.peek_next()
        self.pos += 1
        return value
    
    def peek_next(self)-> str:
        if self.pos + 1 < self.len:
            return self.text[self.pos+1]
    
        return None
    def has_next(self) -> bool:
        return self.pos + 1 < self.len
        
class Solution:
    def calculate(self, s: str) -> int:
        """
        we need to recursively parse the string s 
        we can simply skip all the withespace
        The fact that one operation is allowe to be unary and not the oterh complicates 
        No wait that is not a problem, if s begins with - we simply insert a 0 before it
        Experssion -> Term(("+"|"-")Term)*
        Term -> "("Expression")" | Number
        Number -> -(digits)* | digits 
        """
        #Rmeove all whitespace in s
        s = s.replace(" ", "")
        calculator = CalcParser() 
        return calculator.parse(s)

        
# @lc code=end


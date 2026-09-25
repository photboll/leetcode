# @lc app=leetcode id=1096 slug=brace-expansion-ii lang=python3
#
# [1096] Brace Expansion II
# Difficulty: Hard
# Tags: Hash Table, String, Backtracking, Stack, Breadth-First Search, Sorting
# URL: https://leetcode.com/problems/brace-expansion-ii/
#
# @lc code=start
class Solution:
    def braceExpansionII(self, expression: str) -> list[str]:
        self.i = 0

        
        def parse_expression() :
            # union of terms separated by top-level commas
            result = parse_term()
            while self.i < len(expression) and expression[self.i] == ",":
                self.i += 1
                result |= parse_term()
            return result

        def parse_term():
            #concatenation of factors until "," or "}" or end
            factors = []
            while self.i < len(expression) and expression[self.i] not in ",}":
                factors.append(parse_factor())
            result = {''}
            for f in factors:
                result = {a + b for a in result for b in f}
            return result
        
        def parse_factor():
            if expression[self.i] == "{":
                self.i += 1 # skip opening "{"
                s = parse_expression()
                self.i += 1 # skip closing }
                return s
            else:
                j = self.i
                while j < len(expression) and expression[j].islower():
                    j += 1
                word = expression[self.i:j]
                self.i = j
                return {word}
        
        return sorted(parse_expression())

        

# @lc code=end

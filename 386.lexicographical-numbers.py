#
# @lc app=leetcode id=386 lang=python3
#
# [386] Lexicographical Numbers
#

# @lc code=start
class SolutionBrute:
    def lexicalOrder(self, n:int) -> List[int]:
        return list(map(int, sorted(list(map(str, range(1, n+1))))))
    
class Solution:
    def lexicalOrder(self, n:int) -> List[int]:
        result = []
        
        def dfs(prefix):
            if prefix > n:
                return
            
            result.append(prefix)
            prefix *= 10
            for next_digit in range(10):
                next_prefix = prefix + next_digit
                if next_prefix <= n:
                    dfs(next_prefix)
                else:
                    return 

        for start in range(1, 10):
            dfs(start)

        return result


        
# @lc code=end


#
# @lc app=leetcode id=1871 lang=python3
#
# [1871] Jump Game VII
#

# @lc code=start
class Solution:
    def canReach(self, s, minJump, maxJump):
        n = len(s)
        f = [0] * n
        pre = [0] * n
        f[0]
        for i in range(minJump):
            pre[i] = 1
        
        for i in range(minJump, n):
            left, right = i - maxJump, i - minJump
            if s[i] == "0":
                total = pre[right] - (0 if left <= 0 else pre[left-1])
                f[i] = int(total != 0)
            pre[i] = pre[i-1] + f[i]
        
        return bool(f[-1])

class SolutionV1:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        can_reach = [False] * len(s)
        
        def dfs(pos):
            if can_reach[pos]:
                return 
            for j in range(pos+minJump, min(pos+maxJump+1, len(s))):
                if s[j] == "0":
                    dfs(j)
                    can_reach[j] = True
        
        dfs(0)
        #print(can_reach)

        return can_reach[-1]
                    
        
# @lc code=end


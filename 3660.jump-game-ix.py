#
# @lc app=leetcode id=3660 lang=python3
#
# [3660] Jump Game IX
#

# @lc code=start

from collections import defaultdict, deque

class Solution:
    def maxValue(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [0] * n
        stack = []

        for i in range(n):
            curr_val = nums[i]
            curr_left = i
            curr_right = i

            while stack and stack[-1][0] > nums[i]:
                top_val, top_left, top_right = stack.pop()
                curr_val = max(curr_val, top_val)
                curr_left = top_left
            
            stack.append((curr_val, curr_left, curr_right))
        
        for i in range(len(stack)):
            for j in range(stack[i][1], stack[i][2] + 1):
                result[j] = stack[i][0]
        return result

class SolutionV1:
    def maxValue(self, nums: List[int]) -> List[int]:
         
        n = len(nums)
        edges = defaultdict(list)

        for i in range(n):
            for j in range(i+1, n):
                if nums[j] < nums[i]:
                    edges[i].append(j)
                    edges[j].append(i)
        
        visited  = [False] * n
        result = [0] * n

        for start in range(n):
            if visited[start]:
                continue
            component = []
            q = deque([start])
            mx = nums[start]
            while q:
                i = q.pop()
                component.append(i)
                mx = max(mx, nums[i])
                for neigh in edges[i]:
                    if not visited[neigh]:
                        q.append(neigh)
                        visited[neigh] = True
            
            
            for idx in component:
                result[idx] = mx
        
        return result 

            


        
# @lc code=end


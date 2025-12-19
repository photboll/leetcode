#
# @lc app=leetcode id=2092 lang=python3
#
# [2092] Find All People With Secret
#

# @lc code=start
from collections import  defaultdict
from heapq import heappop, heappush

class Solution:
    def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:

        graph = defaultdict(list)

        for u, v, t in meetings:
            graph[u].append((t, v))
            graph[v].append((t, u))

        
        #The heapueue will only ever hold perons which knows the secret 
        heap = []
        #(time, person)
        heappush(heap, (0, 0))
        heappush(heap, (0, firstPerson))
        visited = [False] * n

        while heap:
            cur_t, u = heappop(heap)
            if visited[u]:
                continue
            visited[u] = True

            for t, v in graph[u]:
                if not visited[v] and t >= cur_t:
                    #dont process duplicates
                    #only people we meet after learning the secret will know it 
                    heappush(heap, (t, v))

        return [i for i in range(n) if visited[i]]

                
            
            


            
            

        
# @lc code=end


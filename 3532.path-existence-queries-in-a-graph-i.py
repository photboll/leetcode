#
# @lc app=leetcode id=3532 lang=python3
#
# [3532] Path Existence Queries in a Graph I
#

# @lc code=start
from collections import defaultdict

class Solution:
    def pathExistenceQueries(self, n: int, nums: List[int], maxDiff: int, queries: List[List[int]]) -> List[bool]:
        """
        is this a union find problem?
        
        Can we interpret the graph as the edges having the weight as the absolut difference between nums[i] and nums[j]
        Then the problem turns into another leetcode 1301 number of paths with a max score. Not really 
        then the problem turns into finding 
        
        no wait. MaxDiff is set from the beginning it does not depend on the query. 
        so n, nums and maxDiff completely defines the graph for all queries.
        then we only need to check if both u and v belongs to the same connected component 

        we let each connected component be represented by its lowest numbered member
        
        """
        
        #belongs_to[i] = u means that i is in the connected component represented by u  
        belongs_to = [0] * n 
        curr_component = 0

        for i in range(1, n):
            #if the difference between adjacent nodes is more than maxdiff
            #they are not connected and we start a new component
            #the input is said to be striclty non-decreasing so once we find one we know that no later indices are connected to it
            if abs(nums[i] - nums[i-1]) > maxDiff:
                curr_component +=1

            belongs_to[i] = curr_component

            

        #print(belongs_to)

        result = []
        for u, v in queries:
            result.append(belongs_to[u] == belongs_to[v])
        return result
            
            
                        


        
        
# @lc code=end


#
# @lc app=leetcode id=2322 lang=python3
#
# [2322] Minimum Score After Removals on a Tree
#

# @lc code=start
from collections import defaultdict
class Solution:
    def minimumScore(self, nums: List[int], edges: List[List[int]]) -> int:
        """
        When we delete a single edge we are left with a subtree of the original and the complement of the subtree.
        deleting two edges will leave us with two subtrees and a remainder.
        can we combine this with XORs propertys to order the edges?
        XOR is associative and commutative. 
        The XOR of any three components will remain constant regardless of how we divide the tree
        This total XOR can easily be computed at the beginning. by XORing every number in nums together 
        The XOR of a subtree remains unchanged when we orphan it by removing an edge.
        CONST = SUB_TREE1 ^ SUB_TREE2 ^ REM
        REM = SUB_TREE1 ^ SUB_TREE2 ^ CONST
        So we can easily compute the score of any deleted edge by using precomputed values. 
        we would still need to evaluate the score of each unorderd pair of edge removals. O(E**2) => O(N**2)
        N can be a maximum of 1000, so a polynomial time algorithm should be enough.
        
        The problem of finding a consistent way to represent each subtree still remains. Can i simply prelable an edge as visited and walk the remaining tree?
        is their a risk that i double count a subtree?
         
        """
        
        n = len(nums)
        adj = defaultdict(list)
        
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        subtree_XOR = [0] * n
        #Single dfs using start/end time technique to determine if any two nodes are ancestors of each other
        start_time = [0] * n
        end_time = [0] * n
        self.timer = 0
        
        def dfs(u, parent):
            start_time[u] = self.timer
            self.timer += 1
            
            #Compute the Xor values depth-first
            current_xor = nums[u]
            for v in adj[u]:
                if v != parent:
                    current_xor ^= dfs(v, u)
            
            #record the current_xor after all children have been processed
            subtree_XOR[u]  = current_xor

            end_time[u] = self.timer
            self.timer += 1

            return current_xor

        
        #We always root the tree at node 0
        total_xor = dfs(0, -1)
        min_score = float("inf")

        for i in range(1, n):
            for j in range(i+1, n):
                #Check ancestry
                is_i_ancestor_of_j = start_time[i] < start_time[j] and end_time[j] < end_time[i]
                is_j_ancestor_of_i = start_time[j] < start_time[i] and end_time[i] < end_time[j]

                xor_i = subtree_XOR[i]
                xor_j = subtree_XOR[j]

                if is_i_ancestor_of_j:
                    #j is in the subtree of i
                    c1 = xor_j
                    c2 = xor_i ^ xor_j
                    c3 = total_xor ^ xor_i
                elif is_j_ancestor_of_i:
                    #i is in the subtree of j
                    c1 = xor_i
                    c2 = xor_j ^ xor_i
                    c3 = total_xor ^ xor_j
                else:# The two removals leeaves a disjoint case 
                    c1 =  xor_i
                    c2 = xor_j
                    c3 = total_xor ^ xor_i ^ xor_j
                
                score = max(c1, c2, c3) - min(c1, c2, c3)
                min_score = min(min_score, score)
        
        return min_score
        
        
                
            
        
# @lc code=end


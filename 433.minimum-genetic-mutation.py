#
# @lc app=leetcode id=433 lang=python3
#
# [433] Minimum Genetic Mutation
#

# @lc code=start
from collections import deque
CHARS = ["A", "C", "G", "T"]

def get_all_mutations(gene):
    for i in range(len(gene)):
        for char in CHARS:
            if gene[i] == char:
                continue
            yield gene[:i] + char + gene[i+1:]
    
class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        if startGene == endGene:
            return 0
        bank = set(bank)
        queue = deque()
        queue.append((startGene, 0))#(Current gene, num mutations)
        visited = set()
        visited.add(startGene)
        while queue:
            curr_gene, num_mutations = queue.popleft()
            if curr_gene == endGene:
                return num_mutations
            
            for mutated_gene in get_all_mutations(curr_gene):
                #is it not seen before and a valid gene
                if mutated_gene not in visited and mutated_gene in bank:
                    visited.add(mutated_gene)
                    queue.append((mutated_gene, num_mutations + 1))
            
            
        
        return -1
# @lc code=end


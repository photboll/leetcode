#
# @lc app=leetcode id=3562 lang=python3
#
# [3562] Maximum Profit from Trading Stocks with Discounts
#

# @lc code=start
from itertools import combinations
from collections import defaultdict
from functools import cache
class Solution:
    def maxProfit(self, n: int, present: List[int], future: List[int], hierarchy: List[List[int]], budget: int) -> int:
        adj = [[] for _ in range(n)]
        for u, v in hierarchy:
            adj[u-1].append(v-1)
        
        # Memoization cache: key = (node_index, parent_bought)
        memo = {}

        def get_dp(u, is_discounted):
            state = (u, is_discounted)
            if state in memo:
                return memo[state]
            
            #Skip buying
            dp_skip = [-float('inf')] * (budget + 1)
            dp_skip[0] = 0 
            
            #try to buy
            cost = present[u]
            if is_discounted:
                cost //= 2
            profit = future[u] - cost
            
            dp_buy = [-float('inf')] * (budget + 1)
            if cost <= budget:
                dp_buy[cost] = profit
            
            # --- Merge Children ---
            for v in adj[u]:
                child_with_discount = get_dp(v, True) # If we bought u, v gets discount
                child_no_discount = get_dp(v, False)  # If we skipped u, v is full price
                
                new_dp_buy = [-float('inf')] * (budget + 1)
                for b_curr in range(budget + 1):
                    if dp_buy[b_curr] == -float('inf'): continue
                    
                    # Iterate up to what fits in the remaining budget
                    for b_child in range(budget - b_curr + 1):
                        if child_with_discount[b_child] > -float('inf'):
                            new_dp_buy[b_curr + b_child] = max(
                                new_dp_buy[b_curr + b_child],
                                dp_buy[b_curr] + child_with_discount[b_child]
                            )
                dp_buy = new_dp_buy

                # Merge logic for dp_skip (We skipped u, so merge with child_no_discount)
                new_dp_skip = [-float('inf')] * (budget + 1)
                for b_curr in range(budget + 1):
                    if dp_skip[b_curr] == -float('inf'): continue
                    
                    for b_child in range(budget - b_curr + 1):
                        if child_no_discount[b_child] > -float('inf'):
                            new_dp_skip[b_curr + b_child] = max(
                                new_dp_skip[b_curr + b_child],
                                dp_skip[b_curr] + child_no_discount[b_child]
                            )
                dp_skip = new_dp_skip

            result = [-float('inf')] * (budget + 1)
            for i in range(budget + 1):
                result[i] = max(dp_buy[i], dp_skip[i])
            
            memo[state] = result
            return result

        # Start DFS from root (node 0), initially not discounted
        final_dp = get_dp(0, False)
        
        return max(0, max(final_dp))
class SolutionV2:
    def maxProfit(self, n: int, present: List[int], future: List[int], hierarchy: List[List[int]], budget: int) -> int:

        adj_list = defaultdict(list)

        for u, v in hierarchy:
            adj_list[u-1].append(v-1)

            
        def merge_states(state1, state2, budget_limit):
            merged = {}
            for cost1, profit1 in state1.items():
                for cost2, profit2 in state2.items():
                    total_cost = cost1 + cost2
                    if total_cost <= budget_limit:
                        total_profit = profit1 + profit2
                        merged[total_cost] = max(merged.get(total_cost, 0), total_profit)
            return merged 
  
        
        @cache
        def dfs(node, discounted):
            cost = present[node] // 2 if discounted else present[node]
            profit = future[node] - cost

            buy_state = {cost: profit} if cost <= budget else {}
            skip_state = {0: 0}

            for child in adj_list[node]:
                if buy_state:
                    buy_state = merge_states(buy_state, dfs(child, True), budget)
                skip_state = merge_states(skip_state, dfs(child, False), budget)

            combined = buy_state.copy()
            for cost, profit in skip_state.items():
                combined[cost] = max(combined.get(cost, 0), profit)

            return combined

        result = dfs(0, False)
        return max(result.values()) if result else 0
        
                    
        
class SolutionV1:
    def maxProfit(self, n: int, present: List[int], future: List[int], hierarchy: List[List[int]], budget: int) -> int:
        children = [[] for _ in range(n)]
        for u, v in hierarchy:
            children[u-1].append(v-1)
        
        profit = [[0,0] for _ in range(n)]
        for i in range(n):
            profit[i][0] = future[i] - present[i]
            profit[i][1] = future[i] - (present[i] // 2)

        dp = [[[ [float("-inf")] * (budget+1) for _ in range(2)
                ] for _ in range(2)
               ] for _ in range(n)
              ]

        visited = [[[False] * 2 for _ in range(2)] for _ in range(n)]


        def dfs(node, bossBuy, buy):
            if visited[node][bossBuy][buy]:
                return
            visited[node][bossBuy][buy] = True


            #cache for current state
            cache = dp[node][bossBuy][buy]

            for i in range(budget +1 ):
                cache[i] = float("-inf")

            if buy:
                cost = present[node] // 2 if bossBuy else present[node]
                cache[cost] = profit[node][bossBuy]
            else:
                cost = 0
                cache[0] = 0
            
            
            # cur = cache copy
            cur = cache[:]

            for v in children[node]:
                dfs(v, buy, 1)
                dfs(v, 0, 0)
                take = dp[v][buy][1]
                skip = dp[v][0][0]

                merged = [float("-inf")] * (budget + 1)

                for b in range(budget + 1):
                    if cur[b] == float("-inf"):
                        continue
                    for x in range(budget - b + 1):
                        best = max(take[x], skip[x])
                        if best != float("-inf"):
                            merged[b + x] = max(
                                merged[b + x],
                                cur[b] + best
                            )

                cur = merged

            dp[node][bossBuy][buy] = cur

        # Root has no boss → bossBuy = 0
        dfs(0, 0, 0)
        dfs(0, 0, 1)

        return max(
            max(dp[0][0][0]),
            max(dp[0][0][1])
        )
        
# @lc code=end


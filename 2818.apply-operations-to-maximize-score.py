#
# @lc app=leetcode id=2818 lang=python3
#
# [2818] Apply Operations to Maximize Score
#

# @lc code=start
from heapq import heapify, heappop
from functools import cache

@cache
def prime_score(num):
    score = 0
    if num % 2 == 0:
        score += 1
        while num % 2 == 0:
            num //= 2
    for p in range(3, int(sqrt(num)) + 1, 2):
        if num % p == 0:
            score += 1
            while num % p == 0:
                num //= p
    if num > 1:
        score += 1
    return score 

def get_prime_scores(nums):
    scores = []
    for num in nums:
        scores.append(prime_score(num))
    return scores

def build_nearest_left_array(prime_scores):
    stack = []#Monotonic increasing stack 
    left = [-1] * len(prime_scores)
    for i in range(len(prime_scores)):
        while stack and prime_scores[stack[-1]] < prime_scores[i]:
            stack.pop()    
        if stack:
            left[i] = stack[-1]
        stack.append(i)
    
    return left

def build_nearest_right_array(prime_scores):
    stack = []
    n = len(prime_scores)
    right = [n] * n
    for i in range(n-1, -1, -1):
        while stack and prime_scores[stack[-1]] <= prime_scores[i]:
            stack.pop()
        if stack:
            right[i] = stack[-1]
        stack.append(i)
    return right

class Solution:
    def maximumScore(self, nums: List[int], k: int) -> int:
        s = get_prime_scores(nums)
        #Build the left array, which holds the nearest index on the left where s[left[i]] >= s[i]
        left = build_nearest_left_array(s)
        right = build_nearest_right_array(s)
        print(f"{s=}\n{left=}\n{right=}")
        
        
        counts = [(right[i] - i) * (i - left[i]) for i in range(len(nums))]
            
        heap = [(-nums[i], counts[i]) for i in range(len(nums))]
        heapify(heap)
        mod = (pow(10, 9) + 7)
        total_score = 1
        while k > 0 and heap:
            num, count = heappop(heap)
            cur_num = - num
            times_chosen = min(count, k)
            total_score = (total_score*pow(cur_num, times_chosen, mod)) % mod
            k -= times_chosen
        return total_score 
# @lc code=end


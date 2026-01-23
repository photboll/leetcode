#
# @lc app=leetcode id=3510 lang=python3
#
# [3510] Minimum Pair Removal to Sort Array II
#

# @lc code=start
from heapq import heappop, heappush, heapify


class Solution:

    def minimumPairRemoval(self, nums: List[int]) -> int:
        n = len(nums)

        #how many elementes are breaking the sorted constraint
        bad_count = sum(nums[i] > nums[i+1] for i in range(n-1))
        if bad_count == 0:
            return 0
        
        #keeps track if nums at remove[i] have been merged into another one already
        remove = [False]*n
        prev = [i - 1 for i in range(n)]
        next = [i+1 if i+1 < n else -1 for i in range(n)]
        

        heap = [(nums[i] + nums[i+1], i) for i in range(n-1)]
        heapify(heap)
        num_ops = 0
        while bad_count > 0:
            #print(bad_count, heap)
            #print(prev)
            #print(next)
            #print(remove)
            pair_sum, i = heappop(heap)

            #lazy delete: skip if we have touched i in another operation
            if remove[i] or next[i] == -1: continue
            #lazy delete: skip if actual sum does not match sum in heap
            j  = next[i]
            if remove[j] or nums[i] + nums[j] != pair_sum: continue

            
            #find the future neighbors of the elements
            # remove old violations
            pi = prev[i]
            if pi != -1 and nums[pi] > nums[i]: bad_count -= 1
            if nums[i] > nums[j] : bad_count -= 1
            nj = next[j]
            if nj != -1 and nums[j] > nums[nj]: bad_count -=1

            
            
            #merge the current number with its neighbor
            nums[i] = pair_sum
            remove[j] = True

            #update pointers 
            next[i] = nj
            if nj != -1:
                prev[nj] = i
            
            
            #check if any new bad pairs have been created, by the merge
            if pi != -1 and nums[pi] >nums[i]: bad_count += 1
            if nj != -1 and nums[i] > nums[nj]: bad_count += 1


            #add the new pairs to the heap
            if pi != -1:
                heappush(heap, (nums[pi] + nums[i], pi))
            
            if nj != -1:
                heappush(heap, (nums[i] + nums[nj], i))
            
            num_ops += 1
        return num_ops
            



        
# @lc code=end


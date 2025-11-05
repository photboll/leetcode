#
# @lc app=leetcode id=3321 lang=python3
#
# [3321] Find X-Sum of All K-Long Subarrays II
#

# @lc code=start
from collections import Counter 
from heapq import heappush, heappop

class Solution:
    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:
        res = []

        #Fill the initial window 
        counts = Counter()
        for i in range(k):
            counts[nums[i]] += 1

        low = []

        for n, c in counts.items():
            heappush(low, (-c, -n))

        value = 0
        top = []
        top_x = set()


        #Move the top x elements to their set
        while len(top_x) < x and low:
            c, n = heappop(low)
            heappush(top, (-c, -n))
            top_x.add(-n)
            value += c * n

        res.append(value)

        def process_num(num):
            if num in top_x:
                heappush(top, (counts[num], num))
            else:
                heappush(low, (-counts[num], -num))

        def clean_low():
            #Lazy delete
            #if the count in the heap does not match the True count in counts.
            #The element have been deleted lazily 
            while low and (counts[-low[0][1]] != -low[0][0] or -low[0][1] in top_x):
                heappop(low)

        def clean_top():
            #Lazy delete
            while top and (counts[top[0][1]] != top[0][0] or top[0][1] not in top_x):
                heappop(top)

        
        #sliding window
        for i in range(k, len(nums)):
            leaving = nums[i - k]
            entering = nums[i]

            if leaving == entering:
                res.append(value)
                continue

            counts[leaving] -= 1
            counts[entering] += 1

            if leaving in top_x:
                value -= leaving

            if entering in top_x:
                value += entering

            #Add the leaving and entering elem to the correct heap
            process_num(leaving)
            process_num(entering)

            #Remove lazy deleted elems from the heaps
            clean_low()
            clean_top()

            
            if low and top:
                #Did the change in counts affect the top_x set?
                #It suffices to compare the top of the heaps 
                if -low[0][0] > top[0][0] or (-low[0][0] >= top[0][0] and -low[0][1] > top[0][1]):
                    new_count, new_top = heappop(low)
                    old_count, old_top = heappop(top)
                    top_x.remove(old_top)
                    top_x.add(-new_top)

                    value -= (old_top * counts[old_top])
                    value += (-new_top * counts[-new_top])
                    heappush(top, (-new_count, -new_top))
                    heappush(low, (-old_count, -old_top))

            clean_low()

            #if there is room in top_x simply moce elems there 
            if low and len(top_x) < x:
                new_count, new_top = heappop(low)
                value += (-new_top * counts[-new_top])
                heappush(top, (-new_count, -new_top))
                top_x.add(-new_top)

            res.append(value)

        return res
            
        
            

        
# @lc code=end


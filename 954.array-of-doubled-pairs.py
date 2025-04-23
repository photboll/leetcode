#
# @lc app=leetcode id=954 lang=python3
#
# [954] Array of Doubled Pairs
#

# @lc code=start
from bisect import bisect_left
from collections import defaultdict
def canReorderIntoPairs(arr, pairing_func= lambda x: 2*x):
        n = len(arr)
        used = [False] * n
        if n % 2 == 1:
            #impossible to reorder an odd nuber of elements into pairs
            return False

        #Holds the indices to arr for each possible number 
        multiset = defaultdict(list)
        for i, num in enumerate(arr):
            multiset[num].append(i)

        for i in range(n):
            if used[i]:
                continue
            #num needs to be paired with a number , func provides the pairing criteria
            pair = pairing_func(arr[i])
            
            if pair is None:
                #The number arr[i] have no valid pairing, but is required 
                return False
            
            indices= multiset[pair]
            if not indices:
                #No number of value pair exists, but it is required
                return False
                
            used[indices.pop()] = True

        return True
            
class Solution:
    def canReorderDoubled(self, arr: List[int]) -> bool:
        """
        Can we greedily remove any arbitrary pair that satisies the condition?
        then it simply reduce to checking. The problem is that we don't know if any arbitrary numer will
        be the smaller or larger one of each pair, Which makes 
        
        Maybe sort it 
        split it in a negative and positive portion. The number of zeros have to be even  
        . when we do them inorder we will know that each current element must be the smaller of the pair,
        when we are considering negative elemnts we are looking for an element that is half of the current 
        When we are considering positve elements we ae looking for an elemnt that is twice of the current
        
        """
        n = len(arr)
        if n % 2 == 1:
            return False
        
        arr.sort()
        last_neg_i = bisect_left(arr, 0)
        neg_arr = arr[:last_neg_i]
        pos_arr = arr[last_neg_i:]

        return canReorderIntoPairs(neg_arr[::-1]) and canReorderIntoPairs(pos_arr)
        
                
        
        
# @lc code=end


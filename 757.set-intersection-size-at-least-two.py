#
# @lc app=leetcode id=757 lang=python3
#
# [757] Set Intersection Size At Least Two
#

# @lc code=start
class Solution:
    def intersectionSizeTwo(self, intervals: List[List[int]]) -> int:
        """
        we go through the intervals in order and we always pick the two largest 
        numbers of each interval to be added to nums. (if additions are necessary)

        checking if we need to add is done by comparing the two largest numbers in nums
        with the currently processed interval. 
        """
        intervals.sort(key= lambda x: (x[1], -x[0]))
        #print(intervals)
        first = intervals[0][1]
        
        containing = [first - 1, first]

        for s, e in intervals[1:]:
            if containing[-2] >= s:
                #the current containing set already 
                #fullfills the criteria for this interval
                continue
            elif containing[-1] >= s:
                #We need to add one more number to the containing set
                containing.append(e)
            else:
                #current interval is not covered by the containing set
                #greedily add the two largest numbers
                containing.extend((e-1, e))
            #print(containing)
            
                
        return len(containing)
            

        
# @lc code=end


#
# @lc app=leetcode id=3394 lang=python3
#
# [3394] Check if Grid can be Cut into Sections
#

# @lc code=start
def mergeOverlappingIntervals(intervals):
    intervals.sort(key= lambda x: x[0])
    noOverlapIntervals = [intervals[0]]
    for i in range(1, len(intervals)):
        #Previous nonoverlappng intervals end time is later than currents start time
        #The overlap 
        if noOverlapIntervals[-1][1] > intervals[i][0]:
            noOverlapIntervals[-1][1] = max(noOverlapIntervals[-1][1], intervals[i][1])
        else:
            noOverlapIntervals.append(intervals[i])
    
    return noOverlapIntervals

def canSplitInK(n, intervals, k):
    #Merge overlapping intervals
    mergedIntervals = mergeOverlappingIntervals(intervals)
    
    return len(mergedIntervals) >= k

class Solution:
    def checkValidCuts(self, n: int, rectangles: List[List[int]]) -> bool:
        #Split the problem in two
        #Try to find two horizontal cuts that satisfies the problem
        #Or Try to findd two Vertiavcal cuts that satisfies the problem 
        #Both of these subproblems should be identical  
        xCoords = list(map(lambda x:[x[0], x[2]], rectangles))
        yCoords = list(map(lambda x:[x[1], x[3]], rectangles))
        if canSplitInK(n, xCoords, 3):
            return True
        if canSplitInK(n, yCoords, 3):
            return True
        
        return False        
# @lc code=end


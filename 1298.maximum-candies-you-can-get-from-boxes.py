#
# @lc app=leetcode id=1298 lang=python3
#
# [1298] Maximum Candies You Can Get from Boxes
#

# @lc code=start
from collections import deque
class Solution:
    def maxCandies(self, status: List[int], candies: List[int], keys: List[List[int]], containedBoxes: List[List[int]], initialBoxes: List[int]) -> int:
        """
        BFS on the current available boxes 
        we need another structure that keeps track of boxes that are currently available to use but  are not open
        Boxes that are available and have status 1, should be added to the queue.
        When we find a key, we change the status of this box to 1 and check if is in our available boxes list
        in which case we move it to the queue.
        When we find new boxes: we check if they are open, in which case we move it to the queue
        else we move it to the available boxes set
        """

        
        tot_candies = 0
        locked_boxes = set()
        q = deque()
        for box in initialBoxes:
            if status[box] == 1:
                q.appendleft(box)
            else:
                locked_boxes.add(box)
                

        while q:
            cur_box = q.pop()
            tot_candies += candies[cur_box]
            
            #Check if the new keys can open any boxes
            for key in keys[cur_box]:
                status[key] = 1
                if key in locked_boxes:
                    locked_boxes.remove(key)
                    q.appendleft(key)

            #check if the containedBoxes can be opened 
            for new_box in containedBoxes[cur_box]:
                if status[new_box] == 1:
                    q.appendleft(new_box)
                else:
                    locked_boxes.add(new_box)
            
        return tot_candies

        
# @lc code=end


#
# @lc app=leetcode id=401 lang=python3
#
# [401] Binary Watch
#

# @lc code=start
from collections import defaultdict

class Solution:
    def __init__(self):
        self.bit_count2times = defaultdict(list)

        for h in range(12):
            for m in range(60):
                num_set = h.bit_count() + m.bit_count()
                self.bit_count2times[num_set].append(f"{h}:{m:02}")
        #print(self.bit_count2times)
                
        

    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        """"  
        Hours: 4 bits 
        Minutes: 6 bits 
        10 bits in total
        of which turnedOn number of bits are set 
        """
        return self.bit_count2times[turnedOn]




        
# @lc code=end


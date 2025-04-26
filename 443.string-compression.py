#
# @lc app=leetcode id=443 lang=python3
#
# [443] String Compression
#

# @lc code=start
class Solution:
    def compress(self, chars: List[str]) -> int:
        n = len(chars)
        if n == 1:
            return 1

        cur_group = chars[0]
        group_size = 0
        new_pos = 0
        for i in range(n):
            if chars[i] == cur_group:
                group_size += 1
                continue
            elif group_size == 1:
                chars[new_pos] = cur_group
            else:
                chars[new_pos] = cur_group
                for digit in str(group_size):
                    new_pos += 1
                    chars[new_pos] = digit

            new_pos += 1
            cur_group = chars[i]
            group_size = 1

        #print(chars)
        chars[new_pos] = cur_group
        if group_size >  1:
            for digit in str(group_size):
                new_pos += 1
                chars[new_pos] = digit
        #print(chars) 
        return new_pos+1       
# @lc code=end


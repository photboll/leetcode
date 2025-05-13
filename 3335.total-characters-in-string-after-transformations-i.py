#
# @lc app=leetcode id=3335 lang=python3
#
# [3335] Total Characters in String After Transformations I
#

# @lc code=start
MOD = pow(10, 9) + 7

class Solution:
    def lengthAfterTransformations(self, s: str, t: int) -> int:
        """
        We only actually care about the number of chars in lthe final string 
        the strging 'a' will double in size after 25? transformations when it turns into "ab"
        "ab" -(24)> "zab" -(1)> "abbc" -(23)> "yzzab" -(1)> "zababbc" -(1)> "abbcbccd"
        dp["a"][0:24] = 1
        dp["a"][25:49] = 2
        dp["a"][]
        Every 25 tranformations the string doubles in length
        The divison will most likely not leave a remainder of 0,
        What happens when t > 25*25
        Pascals triangle shows up as the step sizes in each level of duplication
        """
        freqs = [0] * 26
        for c in s:
            freqs[ord(c) - ord("a")] += 1
        for _ in range(t):
            n_freqs = [0] * 26
            n_freqs[0] = freqs[-1] ## z will turn into as
            # a and z will turn into b
            n_freqs[1] = (freqs[-1] + freqs[0] ) % MOD
            #The count of each char will move over one step 
            for i in range(2, 26):
                n_freqs[i] = freqs[i-1]
            #Update the counts for the next iteration of transformation
            freqs = n_freqs

        return sum(freqs) % MOD

        

# @lc code=end


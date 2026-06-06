#
# @lc app=leetcode id=3753 lang=python3
#
# [3753] Total Waviness of Numbers in Range II
#

# @lc code=start
from functools import cache
class Solution:
    def totalWaviness(self, num1: int, num2: int) -> int:

        def solve(limit):
            if limit < 0:
                return 0

            s = str(limit)

            @cache
            def dfs(pos, tight, started, prev2, prev1):
                if pos == len(s):
                    return (1, 0)

                upper = int(s[pos]) if tight else 9

                total_count = 0
                total_waviness = 0

                for d in range(upper + 1):
                    ntight = tight and d == upper

                    if not started and d == 0:
                        cnt, wav = dfs(
                            pos + 1,
                            ntight,
                            False,
                            10,
                            10
                        )

                        total_count += cnt
                        total_waviness += wav

                    else:
                        if not started:
                            cnt, wav = dfs(
                                pos + 1,
                                ntight,
                                True,
                                10,
                                d
                            )

                            total_count += cnt
                            total_waviness += wav

                        elif prev2 == 10:
                            cnt, wav = dfs(
                                pos + 1,
                                ntight,
                                True,
                                prev1,
                                d
                            )

                            total_count += cnt
                            total_waviness += wav

                        else:
                            peak = prev2 < prev1 > d
                            valley = prev2 > prev1 < d

                            cnt, wav = dfs(
                                pos + 1,
                                ntight,
                                True,
                                prev1,
                                d
                            )

                            total_count += cnt

                            if peak or valley:
                                total_waviness += wav + cnt
                            else:
                                total_waviness += wav
                return total_count, total_waviness
            return dfs(0, True, False, 10, 10)[1]
        return solve(num2) - solve(num1 -1)
        
# @lc code=end


#
# @lc app=leetcode id=2048 lang=python3
#
# [2048] Next Greater Numerically Balanced Number
#

# @lc code=start


from itertools import permutations, combinations
import bisect   
def generate_beautiful_numbers(k_digits):
    s = set()
    words = [
        "1", "22", "333", "4444", "55555", "666666"
    ]
    bases = []
    for r in range(1, len(words)+1):
        for comb in combinations(words, r):
            if sum(len(x) for x in comb) <= k_digits:
                bases.append("".join(comb))
    print(bases)
    
    for base in bases:
        for perm in set(permutations(base)):
            s.add(int("".join(perm)))
    
    return sorted(s)

        
    
class Solution:
    def __init__(self):
        self.beautiful_nums = generate_beautiful_numbers(7)
        print(self.beautiful_nums)

    def nextBeautifulNumber(self, n: int) -> int:
        """
        0 <= n <= 1 000 000
        smallest numverically balanced number strictly greater than n
        
        this woul mean that the largest return value
        will be
        1 224 444
        
        we can select sets of numbers from 
        1, 22, 333, 4444, 55555, 666666  
        7,8,9 and 0 can will be force us outside of the constraints
        
        we need to at leat match the number of digits to n
        It is always better to select the smaler set
        wait i am making this more complicated then it needs to be
        i can just generate all beatiful numbers and sort them and pick the closest one.
        """
        index = bisect.bisect_right(self.beautiful_nums, n)
        return self.beautiful_nums[index]


if __name__ == "__main__":
    sol = Solution()
    for n in [1, 1999, 12312, 1_000_000]:
        print(sol.nextBeautifulNumber(n))


        
# @lc code=end


#
# @lc app=leetcode id=3337 lang=python3
#
# [3337] Total Characters in String After Transformations II
#

# @lc code=start
MOD = pow(10, 9) + 7
ALPHABET_SIZE = 26
def matmul_mod(A: List[List[int]], B: List[List[int]], mod: int)-> List[List[int]]:
    n, m, p = len(A), len(B), len(B[0])
    result = [[0] * p for _ in range(n)]
    for i in range(n):
        for k in range(m):
            for j in range(p):
                result[i][j] = (result[i][j] + A[i][k] * B[k][j]) % mod
    return result

def matpower_mod(A: List[List[int]], p:int, mod:int) -> List[List[int]]:
    result = identity(len(A))
    while p > 0:
        if p % 2 == 1:
            result = matmul_mod(A, result, mod)
        A = matmul_mod(A, A, mod)
        p //= 2
    return result

def identity(n:int) -> List[List[int]]:
    result = [[0]* n for _ in range(n)]
    for i in range(n):
        result[i][i] = 1
    return result

class Solution:
    def lengthAfterTransformations(self, s: str, t: int, nums: List[int]) -> int:
        adj_mat = [[0]* ALPHABET_SIZE for _ in range(ALPHABET_SIZE)]
        for cur_i in range(ALPHABET_SIZE):
            for i in range(nums[cur_i]):
                next_i = (cur_i + 1 + i) % ALPHABET_SIZE
                adj_mat[cur_i][next_i] += 1
        
        init_mat = [[0] * ALPHABET_SIZE]
        for c in s:
            init_mat[0][ord(c) - ord("a")] += 1
        
        #print(init_mat)
        result = matmul_mod(init_mat, matpower_mod(adj_mat, t, MOD), MOD)
        #print(result)
        return sum(result[0]) % MOD
import numpy as np
import numpy.typing as npt

        
class SolutionNP:
    def lengthAfterTransformations(self, s: str, t: int, nums: List[int]) -> int:
        """
        numpy seems to overflow the intermediate results whcih causes the wrong answer
        Cast the probelm as a graph problem,
        The adjencey matrix depends only on how nums looks like, since nums definies how each char will transition to the other chars
        The initial matrix depends only on s, it will have shape 1 x ALPHABET_SIZE
        initial_matrix * (adjecency_matrix)**t should then give how many of each char there will be afterr t transformations
        Simply sum the count of each char and that should be the answer
        """
        def matmul_mod(A:npt.NDArray, B: npt.NDArray, mod: int) -> npt.NDArray:
            return np.matmul(A, B, dtype=np.int64) % mod


        def matpower_mod(A: npt.NDArray, p: int, mod: int) -> npt.NDArray:
            result = np.identity(len(A), dtype=np.int64)
            A = A.copy()
            while p > 0:
                if p % 2 == 1:
                    result = matmul_mod(A, result, mod)
                A = matmul_mod(A, A, mod)
                p //= 2
            return result
        ## Build the adjecency matrix from nums
        adj_mat = np.zeros((ALPHABET_SIZE, ALPHABET_SIZE), dtype=np.int64)
        for cur_i in range(ALPHABET_SIZE):
            for i in range(nums[cur_i]):
                next_i = (cur_i + 1 + i) % ALPHABET_SIZE
                adj_mat[cur_i][next_i] += 1
        #print(adj_mat)

        ## Build the inital matrix 1xALPHABET_SIZE
        init_mat = np.zeros((1, ALPHABET_SIZE), dtype=np.int64)
        for c in s:
            c_i = ord(c) - ord("a")
            init_mat[0][c_i] += 1
        print(init_mat)
                 
        result = matmul_mod(init_mat, matpower_mod(adj_mat, t, MOD), MOD)
        print(result)
        return np.sum(result, dtype=np.int64) % MOD

class SolutionV1:
    def lengthAfterTransformations(self, s: str, t: int, nums: List[int]) -> int:
        """
        This approach is too slow since t can be upto 10**9
        """
        freqs = [0] * ALPHABET_SIZE 
        for c in s:
            freqs[ord(c) - ord("a")] += 1
        
        
        for _ in range(t):
            #print(freqs)
            new_freqs = [0] * ALPHABET_SIZE
            ##Each charcter needs to be expanded according to ums 
            for cur_i in range(ALPHABET_SIZE):
                #teh char corresponding to cur_i will be expanded into the following nums[cur_i] characters
                #cur_i == 0"a" and nums[0] == 3, then each a in freqs will turn into the same number of b's, c's and d's in new_freqs
                for i in range(nums[cur_i]):
                    #To make it wrap around passed the end of the alphabet
                    next_i = (cur_i+1+i) % ALPHABET_SIZE
                    new_freqs[next_i] = (new_freqs[next_i] + freqs[cur_i]) % MOD
            freqs = new_freqs
        print(freqs)
        return sum(freqs) % MOD
                    
                
        
# @lc code=end


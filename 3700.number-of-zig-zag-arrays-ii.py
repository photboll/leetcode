# @lc app=leetcode id=3700 lang=python3
# [3700] Number of ZigZag Arrays II
# @lc code=start

MOD = 1_000_000_007

def matmul(A, B):
    n, m, p = len(A), len(A[0]), len(B[0])
    res = [[0] * p for _ in range(n)]
    for i in range(n):
        for k in range(m):
            r = A[i][k]
            if r == 0:
                continue
            for j in range(p):
                res[i][j] = (res[i][j] + r * B[k][j]) % MOD
    return res

def matpow(A, exp, init):
    result = init
    base = A
    while exp > 0:
        if exp & 1:
            result = matmul(result, base)
        base = matmul(base, base)
        exp >>= 1
    return result

class Solution:
    def zigZagArrays(self, n: int, l: int, r: int) -> int:
        m = r - l + 1
        if n == 1:
            return m
        size = 2 * m
        u = [[0] * size for _ in range(size)]
        for i in range(m):
            for j in range(i):
                u[i][j + m] = 1          # state i (high), go to low j < i
            for j in range(i + 1, m):
                u[i + m][j] = 1          # state m+i (low), go to high j > i
        dp = matpow(u, n - 1, [[1] * size])
        return sum(dp[0]) % MOD


MOD = pow(10, 9) + 7
class SolutionTLE:
    def zigZagArrays(self, n: int, l: int, r: int) -> int:
        m = r - l + 1
        if n == 1:
            return m

        size = 2 * m
        u = [[0] * size for _ in range(size)]

        for i in range(m):
            for j in range(i + 1, m):
                u[i][j + m] = 1
            for j in range(i):
                u[m + i][j] = 1

        mat = matpow(u, n - 1, size)

        result = 0
        for i in range(size):
            for j in range(size):
                result = (result + mat[i][j]) % MOD

        return result


class SolutionTLE2:
    def zigZagArrays(self, n: int, l: int, r: int) -> int:
        m = r - l + 1
        if n == 1:
            return m

        # after placing first element: all states valid, count = 1 each
        up = [1] * m   # up[i]: ends at i, next must go up
        dn = [1] * m   # dn[i]: ends at i, next must go down

        for _ in range(n - 1):
            # prefix sum of up: pre_up[j] = sum(up[0..j-1])
            pre_up = [0] * (m + 1)
            for i in range(m):
                pre_up[i + 1] = (pre_up[i] + up[i]) % MOD

            # suffix sum of dn: suf_dn[j] = sum(dn[j+1..m-1])
            suf_dn = [0] * (m + 1)
            for i in range(m - 1, -1, -1):
                suf_dn[i] = (suf_dn[i + 1] + dn[i]) % MOD

            new_dn = [pre_up[j] for j in range(m)]       # sum up[i] for i < j
            new_up = [suf_dn[j + 1] for j in range(m)]   # sum dn[i] for i > j

            up, dn = new_up, new_dn

        return sum(up + dn) % MOD       

# @lc code=end


#
# @lc app=leetcode id=1622 lang=python3
#
# [1622] Fancy Sequence
#

# @lc code=start
MOD = pow(10, 9) + 7
class Fancy:

    def __init__(self):
        self.val = []
        self.a = 1
        self.b = 0
     
    def append(self, val:int) -> None:
        x = (val - self.b + MOD) % MOD
        self.val.append(x * pow(self.a, MOD-2, MOD) % MOD)

    def addAll(self, inc: int) -> None:
        self.b = (self.b + inc) % MOD

        

    def multAll(self, m: int) -> None:
        self.a = (self.a * m ) % MOD
        self.b = (self.b * m ) % MOD

    def getIndex(self, idx: int) -> int:
        if idx >= len(self.val):
            return -1
        return (self.a*self.val[idx] + self.b) % MOD
        


# Your Fancy object will be instantiated and called as such:
# obj = Fancy()
# obj.append(val)
# obj.addAll(inc)
# obj.multAll(m)
# param_4 = obj.getIndex(idx)
# @lc code=end


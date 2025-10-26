#
# @lc app=leetcode id=2043 lang=python3
#
# [2043] Simple Bank System
#

# @lc code=start
class Bank:

    def __init__(self, balance: List[int]):
        self.accounts = {i+1:num for i, num in enumerate(balance)}
        

    def transfer(self, account1: int, account2: int, money: int) -> bool:
        if self.withdraw(account1, money):
            if self.deposit(account2, money):
                return True
            else:
                #return the money if the deposit fails
                self.deposit(account1, money)
        
        return False
        
        

    def deposit(self, account: int, money: int) -> bool:
        if account in self.accounts and money >= 0:
            self.accounts[account] += money
            return True
        return False
        

    def withdraw(self, account: int, money: int) -> bool:
        if account in self.accounts and 0 <= money <= self.accounts[account]:
            self.accounts[account] -= money
            return True
        return False
        


# Your Bank object will be instantiated and called as such:
# obj = Bank(balance)
# param_1 = obj.transfer(account1,account2,money)
# param_2 = obj.deposit(account,money)
# param_3 = obj.withdraw(account,money)
# @lc code=end


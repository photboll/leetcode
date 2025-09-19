#
# @lc app=leetcode id=3484 lang=python3
#
# [3484] Design Spreadsheet
#

# @lc code=start
class Spreadsheet(object):

    def __init__(self, rows):
        self.map = {}

    def setCell(self, cell, value):
        self.map[cell] = value

    def resetCell(self, cell):
        self.map[cell] = 0

    def getValue(self, formula):
        formula = formula[1:]
        for i in range(len(formula)):
            if formula[i] == '+':
                s1, s2 = formula[:i], formula[i+1:]
                left = self.map.get(s1, 0) if s1[0].isupper() else int(s1)
                right = self.map.get(s2, 0) if s2[0].isupper() else int(s2)
                return left + right

        return 0

        


# Your Spreadsheet object will be instantiated and called as such:
# obj = Spreadsheet(rows)
# obj.setCell(cell,value)
# obj.resetCell(cell)
# param_3 = obj.getValue(formula)
# @lc code=end


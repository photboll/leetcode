#
# @lc app=leetcode id=2069 lang=python3
#
# [2069] Walking Robot Simulation II
#

# @lc code=start
DIRECTIONS = [(0, 1, "North"), (1, 0, "East"), (0, -1, "South"), (-1, 0, "West")]# N, E, S ,W
class Robot:

    def __init__(self, width: int, height: int):
        self.h = height
        self.w = width
        self.P= 2 * (self.h + self.w)
        self.has_moved = False
        self.pos = 0
        

    def step(self, num: int) -> None:
        self.has_moved = True
        self.pos = (self.pos + num) % self.P

    def getPos(self) -> List[int]:
        if self.pos <= self.w : return [self.pos, 0]
        elif self.pos <= (self.w+self.h): return [self.w, self.pos - self.w]
        elif self.pos <= (2* self.w + self.h): return [self.w - (self.pos - (self.w+self.h)), self.h]
        return [0, self.h -(self.pos (2* self.w + self.h))]
        

    def getDir(self) -> str:
        if not self.has_moved: return "East"
        if self.pos == 0: return "South"#
# @lc app=leetcode id=2069 lang=python3
#
# [2069] Walking Robot Simulation II
#

# @lc code=start
DIRECTIONS = [(0, 1, "North"), (1, 0, "East"), (0, -1, "South"), (-1, 0, "West")]# N, E, S ,W
class Robot:

    def __init__(self, width: int, height: int):
        self.h = height
        self.w = width
        self.P= 2 * (self.h + self.w)
        self.has_moved = False
        self.pos = 0
        

    def step(self, num: int) -> None:
        self.has_moved = True
        self.pos = (self.pos + num) % self.P

    def getPos(self) -> List[int]:
        if self.pos <= self.w : return [self.pos, 0]
        elif self.pos <= (self.w+self.h): return [self.w, self.pos - self.w]
        elif self.pos <= (2* self.w + self.h): return [self.w - (self.pos - (self.w+self.h)), self.h]
        return [0, self.h -(self.pos (2* self.w + self.h))]
        

    def getDir(self) -> str:
        if not self.has_moved: return "East"
        if self.pos == 0: return "South"
        if self.pos <= self.w: return "East"#
# @lc app=leetcode id=2069 lang=python3
#
# [2069] Walking Robot Simulation II
#

# @lc code=start
DIRECTIONS = [(0, 1, "North"), (1, 0, "East"), (0, -1, "South"), (-1, 0, "West")]# N, E, S ,W
class Robot:

    def __init__(self, width: int, height: int):
        self.h = height -1
        self.w = width -1
        self.P= 2 * (self.h + self.w)
        self.has_moved = False
        self.pos = 0
        

    def step(self, num: int) -> None:
        self.has_moved = True
        self.pos = (self.pos + num) % self.P

    def getPos(self) -> List[int]:
        if self.pos <= self.w : return [self.pos, 0]
        elif self.pos <= (self.w+self.h): return [self.w, self.pos - self.w]
        elif self.pos <= (2* self.w + self.h): return [self.w - (self.pos - (self.w+self.h)), self.h]
        return [0, self.h -(self.pos - (2* self.w + self.h))]
        

    def getDir(self) -> str:
        if not self.has_moved: return "East"
        if self.pos == 0: return "South"
        if self.pos <= self.w: return "East"
        if self.pos <= self.w+self.h: return "North"
        if self.pos <= (2*self.w + self.h): return "West"
        return "South"
        if self.pos <= self.w+self.h: return "North"
        if self.pos <= (2*self.w + self.h): return "West"
        return "South"
        if self.pos <= self.w: return "East"
        if self.pos <= self.w+self.h: return "North"
        if self.pos <= (2*self.w + self.h): return "West"
        return "South"
        


# Your Robot object will be instantiated and called as such:
# obj = Robot(width, height)
# obj.step(num)
# param_2 = obj.getPos()
# param_3 = obj.getDir()
# @lc code=end


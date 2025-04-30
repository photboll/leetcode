#
# @lc app=leetcode id=841 lang=python3
#
# [841] Keys and Rooms
#

# @lc code=start
class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        n = len(rooms)
        visited = [False] * n
        stack = [0] # Cur room  
        visited[0] = True

        while stack:
            cur_room = stack.pop()
            for next_room in rooms[cur_room]:
                if not visited[next_room]:
                    visited[next_room] = True
                    stack.append(next_room)
        return sum(visited) == n
        
# @lc code=end


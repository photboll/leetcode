#
# @lc app=leetcode id=3433 lang=python3
#
# [3433] Count Mentions Per User
#

# @lc code=start
from collections import deque

class Solution:
    def countMentions(self, numberOfUsers: int, events: List[List[str]]) -> List[int]:
        online = [True] * numberOfUsers
        mentions = [0] * numberOfUsers

        def pre_process(events):
            for i in range(len(events)):
                events[i][1] = int(events[i][1])
            
            events.sort(key=lambda x: x[0], reverse=True)
            events.sort(key= lambda x: x[1])
            return events
            
        events = pre_process(events)

        #queue to hold (timestamp, id) of when user id will go online again 
        q = deque()
        all_count = 0

        def user2id(user):
            return int("".join(user[2:]))

        for msg_type, t, data in events:
            #process the users that will come back online 
            while q and q[0][0] <= t:
                _, user = q.popleft()
                online[user] = True
            
            #process message type
            if msg_type == "MESSAGE":
                if data == "ALL":
                    all_count += 1
                elif data =="HERE":
                    for user in range(numberOfUsers):
                        mentions[user] += online[user]
                else:
                    for user in map(user2id, data.split(" ")):
                        mentions[user] += 1
                    
            elif msg_type == "OFFLINE":
                user = int(data)
                online[user] = False
                q.append((t+60, user))
        
        return [cnt + all_count for cnt in mentions]
                
            





        
        
# @lc code=end


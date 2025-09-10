#
# @lc app=leetcode id=1733 lang=python3
#
# [1733] Minimum Number of People to Teach
#

# @lc code=start
from collections import Counter
class Solution:
    def minimumTeachings(self, n: int, languages: List[List[int]], friendships: List[List[int]]) -> int:
        """
        We can only choose ONE language to teach. This simplifies the problem a bit
        
        A worst case scenario is that two friends both have to learn the new language
        We can start with filtering out all friendships which already have language in common
        Since they will not affect the solution.
        
        Can we just count how many people speak each language?
        No, it is possible for someone to not know the language we are teaching without breaking the conditions

        """
        for i in range(len(languages)):
            languages[i] = set(languages[i])
        
        users_to_teach = set()
    
        for u, v in friendships:
            u -= 1
            v -= 1
            if len(languages[u].intersection(languages[v])) == 0:
                users_to_teach.add(u)
                users_to_teach.add(v)


        
        counts = [0] * (n+1)
        for user in users_to_teach:
            for lang in languages[user]:
                counts[lang] += 1
        
        return len(users_to_teach) - max(counts)
            
        

            
        
# @lc code=end


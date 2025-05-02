#
# @lc app=leetcode id=838 lang=python3
#
# [838] Push Dominoes
#

# @lc code=start
class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        """
        can we use dp?
        base case: all dominoes of length one willl always stay the same 
        "RR.L" -> "RR.L
        the solution for "RR." is not very helpful here since it is "RRR"
        we might the los the time aspect if we try to do dp
        can we tell locally waht will happen to a domino?
        "..." -> "..."
        "L.." -> "LL."
        "L.R" -> "L.R"
        "R.L" -> "R.L"
        At teach time step we can inspect each indivudl . and check its neighbors
        keep doing so until nothing changes in time step
        .
        this seems unnecessaily slow
        
        Consider a standing domino "." can we tell which we it should fall immediately?
        It will fall in the same direction as the closest falling domino.
        maybe do it in a double pass like trapping rainwater.
        There are two cases where a domino will keep standing,
        1. There is a tie between closest L and closest R, so the forces cancel each other
        2. No other domino interacts with it
        
        """
        n = len(dominoes)
        dominoes = [dom for dom in dominoes]
        prefix_r = [-1] * n #-1 means that there will be no dominon falling towards the right here 
        prev_r = -1
        for i in range(n):
            if dominoes[i] == "R":
                prev_r = i
            elif dominoes[i] == "L":
                prev_r = -1
            
            prefix_r[i] = prev_r
        #print("".join(dominoes))
        #print("R",prefix_r)

        suffix_l = [-1] * n
        prev_l = -1
        for i in range(n-1,-1,-1):
            if dominoes[i] == "L":
                prev_l = i
            elif dominoes[i] == "R":
                prev_l = -1
            suffix_l[i] = prev_l
            
        #print("L",suffix_l)
        
        #Now we shold be able to use prefix_r and suffix_l 
        #To determine what is closest for each "."
        for i in range(n):
            if dominoes[i] == ".":
                #What will happen to this domino?
                if prefix_r[i] < 0 and suffix_l[i] < 0:
                    #No domino is falling towards i
                    #print(i)
                    continue
                elif prefix_r[i] < 0:
                    #There is only domions falling towards the left 
                    #So this domino must also fall to the left
                    dominoes[i] = "L"
                elif suffix_l[i] < 0:
                    #There is onlu domiones falling towards the right
                    #This domion will also fall right
                    dominoes[i]  = "R"
                else:
                #we have both dominoes falling towards the right and left here 
                # Who wins? 
                    dist_r = i - prefix_r[i]
                    dist_l = suffix_l[i] - i
                    #print(i, dist_l, dist_r, prefix_r[i], suffix_l[i])
                    if dist_l < dist_r:
                        dominoes[i] ="L"
                    elif dist_l > dist_r:
                        dominoes[i] = "R"
                    else:
                        #There is a tie, the forces will cancle out
                        dominoes[i] = "."
        
        
        #print("".join(dominoes))
        
        return "".join(dominoes)

        
        
# @lc code=end


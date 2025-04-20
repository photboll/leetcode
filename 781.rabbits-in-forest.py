#
# @lc app=leetcode id=781 lang=python3
#
# [781] Rabbits in Forest
#

# @lc code=start
class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        #The frequence of occurence of each answers matters
        #Bunnies of the same color will anwer the same
        #But bunnies of different colors might also have the same answer, surjective, 
        #Since we want a minimum value we can always try to say that bunnies with identical answers belong to the same color
        #But it is possible that there are more identical answers then a single color group can fit
        # The answers [1, ,1 ,1] would require at least two colrings, example where the first two bunnies have the same coloring 
        #but the third can't also have this colloring since then they would have answer 2 and not 1
        answers.sort()
        n = len(answers)
        min_rabbits = 1
        unseen_rabbits_of_cur_color = answers[0]
        #print(answers)
        for i in range(1, n):
            #The current rabbit must belong to a coloring as wel
            min_rabbits += 1
            if answers[i] != answers[i-1] or unseen_rabbits_of_cur_color == 0:
                #then we need a new color for this rabbit
                #The remaining unssen rabits can't have ansewerd
                #But we know they must exist so we add them to the count
                min_rabbits += unseen_rabbits_of_cur_color
                #print("New Color", i, min_rabbits)
                unseen_rabbits_of_cur_color = answers[i]
            else:
                #This rabbit can have the same color as the previously asked
                #So we have seen another rabbit of the current coloring 
                unseen_rabbits_of_cur_color -= 1
        
        min_rabbits += unseen_rabbits_of_cur_color 
        return min_rabbits 
        
        
# @lc code=end


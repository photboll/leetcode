#
# @lc app=leetcode id=2353 lang=python3
#
# [2353] Design a Food Rating System
#

# @lc code=start

from heapq import heapify, heappush, heappop
from collections import defaultdict
    
class FoodRatings:
    """
    We are only interested in querying for the highest rated one. 
    it is not sufficient to only keep track of the currently highest rated dish of each cuisine.
    As it is possible that its rating may be lowered. which would require us to search 
    through all dishes of that cusine to find the new maximum
    
    a dictionary of heaps can be used to efficiently keep track of the order.
    but it will be hard to update a dishs rating, since we need to look through the entire heap to find it.
    might still be useful in combination with another dict. No this would require implementing an custom indexed heap
    
    a dictionary of sorted linked lists. easy to find the max. hard to find the element which needs to be updated
    
    a i overthinking this? it might be good enough to keep dishes sorted and simply re arrange 
    
    
    FInal approach I will use a heap for each cuisine and keep a separate food:rating dict.
    when updating ratings i will simply append the new food and rating to the heap. Not bothering to delete the old one
    when reading from the heap I will verify that the popped value matches the dicts value
    if not I will simple keep popping.
    This will cause the heaps to be unnecessarily big, but it saves me from modifying inplace 
    """
    def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
        self.food_rating = {}
        self.food_cuisine = {}
        self.lookup = defaultdict(list)
        self.size = len(foods)

        for i in range(self.size):
            #-ratigns[i] because heapq is a min-heap
            food_obj = (-ratings[i], foods[i])
            self.lookup[cuisines[i]].append(food_obj)
            self.food_rating[foods[i]] = food_obj
            self.food_cuisine[foods[i]] = cuisines[i]
        
        for k in self.lookup:
            heapify(self.lookup[k])
        

    def changeRating(self, food: str, newRating: int) -> None:
        food_obj = (-newRating, food)
        self.food_rating[food] = food_obj
        cuisine = self.food_cuisine[food]
        heappush(self.lookup[cuisine], food_obj)

    def highestRated(self, cuisine: str) -> str:
        heap = self.lookup[cuisine]
        #Pop all stale entries 
        while heap and heap[0] != self.food_rating[heap[0][1]]:
            #print("Stale value", heap[0], "Actual: ", self.food_rating[heap[0][1]])
            #print(heap)
            heappop(heap)

        #return the name of the top of the heap 
        return heap[0][1]
        


# Your FoodRatings object will be instantiated and called as such:
# obj = FoodRatings(foods, cuisines, ratings)
# obj.changeRating(food,newRating)
# param_2 = obj.highestRated(cuisine)
# @lc code=end


#
# @lc app=leetcode id=1912 lang=python3
#
# [1912] Design Movie Rental System
#

# @lc code=start
from heapq import heappop, heappush, heapify
from collections import defaultdict

class MovieRentingSystem:
    """
    A movie heap for unrented movies, min-heap, (price, shop). rentable
    a global heap for currently rented movies, min-heap, (price, shop, movie), rented
    Use lazy deletion if necessary.
    
    When a movie gets rented:
        mark entry in rentable as deleted
        add it to rented heap
    when a move gets dropped:
        mark entry in rented as deleted
        add it it to rentable
        
    for search and report we have to check if the current best entry is still availalbe in the respective heap 
        

    """

    def __init__(self, n: int, entries: List[List[int]]):
        self.price_list = {}
        self.rentable = defaultdict(list)
        self.on_loan = set()
        self.rented = []

        for shop, movie, price in entries:
            self.rentable[movie].append((price, shop))
            self.price_list[(shop, movie)] = price
        
        for heap in self.rentable.values():
            heapify(heap)

    def search(self, movie: int) -> List[int]:
        heap = self.rentable[movie]
        result = []
        #hold entries that need to be added back to heap
        tmp = []
        while heap and len(result)< 5:
            price, shop = heappop(heap)
            if (shop, movie) not in self.on_loan and shop not in result:
                result.append(shop)
                tmp.append((price, shop))

        #put back the valid entries
        for entry in tmp:
            heappush(heap, entry)

        return result

    def rent(self, shop: int, movie: int) -> None:
        self.on_loan.add((shop, movie))
        price = self.price_list[(shop, movie)]
        heappush(self.rented, (price, shop, movie))
        

    def drop(self, shop: int, movie: int) -> None:
        self.on_loan.remove((shop, movie))
        price = self.price_list[(shop, movie)]
        heappush(self.rentable[movie], (price, shop))
        

    def report(self) -> List[List[int]]:
        result = []
        heap = self.rented

        #tmp to hold valid entries
        tmp = []
        while heap and len(result) < 5:
            price, shop, movie = heappop(heap)
            if (shop, movie) in self.on_loan and (shop, movie) not in result:
                result.append((shop, movie))
                tmp.append((price, shop, movie))
        
        #add valid entries back to heap
        for entry in tmp:
            heappush(heap, entry)
        return result


# Your MovieRentingSystem object will be instantiated and called as such:
# obj = MovieRentingSystem(n, entries)
# param_1 = obj.search(movie)
# obj.rent(shop,movie)
# obj.drop(shop,movie)
# param_4 = obj.report()
# @lc code=end


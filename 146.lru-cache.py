#
# @lc app=leetcode id=146 lang=python3
#
# [146] LRU Cache
#
# https://leetcode.com/problems/lru-cache/description/
#
# algorithms
# Medium (44.67%)
# Likes:    21683
# Dislikes: 1121
# Total Accepted:    2M
# Total Submissions: 4.6M
# Testcase Example:  '["LRUCache","put","put","get","put","get","put","get","get","get"]\n' +'[[2],[1,1],[2,2],[1],[3,3],[2],[4,4],[1],[3],[4]]'
#
# Design a data structure that follows the constraints of a Least Recently Used
# (LRU) cache.
# 
# Implement the LRUCache class:
# 
# 
# LRUCache(int capacity) Initialize the LRU cache with positive size
# capacity.
# int get(int key) Return the value of the key if the key exists, otherwise
# return -1.
# void put(int key, int value) Update the value of the key if the key exists.
# Otherwise, add the key-value pair to the cache. If the number of keys exceeds
# the capacity from this operation, evict the least recently used key.
# 
# 
# The functions get and put must each run in O(1) average time complexity.
# 
# 
# Example 1:
# 
# 
# Input
# ["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
# [[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
# Output
# [null, null, null, 1, null, -1, null, -1, 3, 4]
# 
# Explanation
# LRUCache lRUCache = new LRUCache(2);
# lRUCache.put(1, 1); // cache is {1=1}
# lRUCache.put(2, 2); // cache is {1=1, 2=2}
# lRUCache.get(1);    // return 1
# lRUCache.put(3, 3); // LRU key was 2, evicts key 2, cache is {1=1, 3=3}
# lRUCache.get(2);    // returns -1 (not found)
# lRUCache.put(4, 4); // LRU key was 1, evicts key 1, cache is {4=4, 3=3}
# lRUCache.get(1);    // return -1 (not found)
# lRUCache.get(3);    // return 3
# lRUCache.get(4);    // return 4
# 
# 
# 
# Constraints:
# 
# 
# 1 <= capacity <= 3000
# 0 <= key <= 10^4
# 0 <= value <= 10^5
# At most 2 * 10^5 calls will be made to get and put.
# 
# 
#

# @lc code=start
class ListNode:
    def __init__(self,key, val, next=None, prev=None):
        self.key = key
        self.val = val
        self.next = next
        self.prev = prev
    def __repr__(self):
        return f"{self.key} = {self.val}"

class LRUCache:
    def __init__(self, capacity: int):
      self.capacity = capacity
      self.cache = {}
      self.tail = ListNode(-1, -1)
      self.head = ListNode(-1, -1)
      self.head.next = self.tail
      self.tail.prev = self.head
      
    def append(self, node: ListNode):
        """
        Appends the node the the front of the list, most recently used position
        """
        next_node = self.head.next
        self.head.next = node
        node.prev = self.head
        node.next = next_node
        next_node.prev = node
    
    def remove(self, node: ListNode):
        """
        Removes a node from the doulby linked list 
        """
        prev_node = node.prev
        next_node = node.next
        prev_node.next = next_node
        next_node.prev = prev_node
        #Orphan the current node 
        node.next = None
        node.prev = None
        
      
    def get(self, key: int) -> int:
        #print("Getting", key)
        if key not in self.cache:
          return -1

        node = self.cache[key]
        #Mark the key as used recently, by simply removing it and adding it at the head 
        self.remove(node)
        self.append(node)
        return node.val
    
    def put(self, key: int, value: int) -> None:
        #print("Putting", key, value)
        if key in self.cache:
           node = self.cache[key]
           self.remove(node)
           del self.cache[key]
        #Evict node if needed 
        if len(self.cache) >= self.capacity:
            lru_node = self.tail.prev #Find the LRU
            self.remove(lru_node)
            del self.cache[lru_node.key] #Remove it from the cache
            
             
        #add the key, value pair to the cache and update lru list
        new_node = ListNode(key, value)
        self.cache[key] = new_node 
        self.append(new_node)
        #print(self.cache)
        
        

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
# @lc code=end


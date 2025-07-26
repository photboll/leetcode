

class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1 # For AVL balancing 
        self.size = 1 # For order statistics (count of nodes in subtree)
        

class OrderStatisticsAVLTree:
    def _get_height(self, node):
        return node.height if node else 0

    def _get_size(self, node):
        return node.size if node else 0
    
    def _update_node_properties(self, node):
        node.height = 1 + max(self._get_height(node.left), self._get_height(node.right))
        node.size = 1 + self._get_size(node.left) + self._get_size(node.right)
    
    def _get_balance(self, node):
        return self._get_height(node.left) - self._get_height(node.right) if node else 0
    
    def _right_rotate(self, y):
        x = y.left
        T2 = x.right
        x.right = y
        y.left = T2
        self._update_node_properties(x)
        self._update_node_properties(y)
        return x
    
    def _left_rotate(self, x):
        y = x.right
        T2 = y.left
        y.left = x
        x.right = T2
        self._update_node_properties(x)
        self._update_node_properties(y)
        return y
    
    def _rebalance(self, root):
        #Rebalance the nodes if necessary
        self._update_node_properties(root)
        balance = self._get_balance(root) 
        
        #Left heavy cases 
        if balance > 1:
            if self._get_balance(root.left) < 0: #Left-Right case
                root.left = self._left_rotate(root.left)
            return self._right_rotate(root)#Left-Left case
        
        #Right heavy cases
        if balance < -1:
            if self._get_balance(root.right) > 0:#Right-Left case
                root.right = self._right_rotate(root.right)
            return self._left_rotate(root)# Right-Right case

        
        return root
    def insert(self, root, key):
        if not root:
            return Node(key)
        
        if key < root.key:
            root.left = self.insert(root.left, key)
        else:
            root.right = self.insert(root.right, key)
        
        return self._rebalance(root)
        
    def find_min_node(self, node):
        curr = node
        while curr.left is not None:
            curr = curr.left
        return curr 
    
    def delete(self, root, key):
        if not root:
            return root
        
        if key < root.key:
            root.left = self.delete(root.left, key)
        elif key > root.key:
            root.right = self.delete(root.right, key)
        else:#The roots key is the key we want to delete
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left

            #The node have two children
            #The smallest node in the right subtree is the node with root.rank() + 1
            temp = self.find_min_node(root.right)
            root.key = temp.key
            root.right = self.delete(root.right, temp.key)
        
        if root is None:
            return root
        
        return self._rebalance(root)
    
    def select(self, root, k):
        """Finds the kth smallest element (1-indexed)"""
        if not root:
            return None
        
        left_size = self._get_size(root.left)
        rank = left_size + 1
        if k == rank:
            return root.key
        elif k < rank:
            return self.select(root.left, k)
        else:
            return self.select(root.right, k - rank)


class TopKTracker:
    def __init__(self, k):
        if k <= 0:
            raise ValueError("K must be positive")
        self.k = k
        self.tree = OrderStatisticsAVLTree()
        self.root = None
    
    def add(self, element):
        """
        adds an element to the tracker in O(Log K) time
        """
        current_size = self.tree._get_size(self.root)

        if current_size < self.k:
            self.root = self.tree.insert(self.root, element)
        else:
            min_val = self.tree.find_min_node(self.root).key
            if element > min_val:
                self.root = self.tree.insert(self.root, element)
                self.root = self.tree.delete(self.root, min_val)
    
    def get_ith_largest(self, i):
        """
        Returns the i-th largest element (1-indexed) in O(log k) time
        
        """
        current_size = self.get_size()
        if not (1<= i <= current_size):
            raise IndexError(f"{i=} is out of bounds. {current_size=}")
        
        return self.tree.select(self.root, current_size-i + 1)
        
        
    
    def get_size(self):
        return self.tree._get_size(self.root)
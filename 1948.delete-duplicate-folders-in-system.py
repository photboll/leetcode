#
# @lc app=leetcode id=1948 lang=python3
#
# [1948] Delete Duplicate Folders in System
#

# @lc code=start
from collections import Counter
class Trie:
    serial = ""
    def __init__(self):
        self.children = {}

class Solution:
    def deleteDuplicateFolder(self, paths: List[List[str]]) -> List[List[str]]:
        root = Trie()
        for path in paths:
            curr = root
            for node in path:
                if node not in curr.children:
                    curr.children[node] = Trie()
                curr = curr.children[node]
        
        
        freqs = Counter()


        def construct(node: Trie) -> None:
            """
            Construct the serialized representation of the node(s)
            """
            #Leaf nodes have an empty serialization
            if not node.children:
                return 
            
            v = []

            #FInd the serailized representation of node
            for folder, child in node.children.items():
                construct(child)
                v.append(f"{folder}({child.serial})")
            
            v.sort()
            node.serial = "".join(v)
            freqs[node.serial] += 1
        
        construct(root)
        result = []
        path = []

        def operate(node:Trie):
            """
            duplicate serializations need to be remove/ not added to the outpu
            """
            if freqs[node.serial] > 1:
                return
            
            if path:
                result.append(path[:])
            
            for folder, child in node.children.items():
                path.append(folder)
                operate(child)
                path.pop()
            
        operate(root)

        return result
                

        
# @lc code=end


"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:

        output = []
        def treverse(root,output):
            if not root: return
            output.append(root.val)
            
            #  here , iterate over the all children and call recursive treverse on each one of them.
            for i in root.children:
                treverse(i,output)

        treverse(root,output)
        return output
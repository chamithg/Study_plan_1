# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        #  create a hashmap to store nodes by levels.
        nodeHash = {}
        
        
        def treverse(node,level):
            if not node: return
            # append value to appropriate level array
            if level not in nodeHash.keys():
                nodeHash[level] = []
            nodeHash[level].append(node.val)
            # increase level by one in each iteration.
            treverse(node.left, level+1)
            treverse(node.right, level+1)

        treverse(root,0)
        output = []

        for i in nodeHash.values():
            output.append(i)

        return output
        


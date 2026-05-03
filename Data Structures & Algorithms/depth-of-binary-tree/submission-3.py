# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        stack = [[root, 1]]
        res = 0

        while stack:
            for i in range(len(stack)):
                node, level = stack.pop()
                if node:
                    res = max(res, level)

                    if node.left:
                        stack.append([node.left, level + 1])
                    if node.right:
                        stack.append([node.right, level + 1])
        
        return res

                

            


        

        
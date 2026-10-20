# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.diameter = 0
        self.dfs(root)
        if not root:
            return 0
        
        return self.diameter

        
    def dfs(self, node):
        if not node:
            return 0
        if not node.left and not node.right:
            return 1
        left = self.dfs(node.left)
        right = self.dfs(node.right)

        self.diameter = max(self.diameter , left + right)

        return 1 + max(left, right)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def __init__(self):
        self.maxSum = 0
    def bstToGst(self, root: TreeNode) -> TreeNode:
        if not root:
            return None
        root.right = self.bstToGst(root.right)
        self.maxSum += root.val
        root.val = self.maxSum
        root.left = self.bstToGst(root.left)
        return root
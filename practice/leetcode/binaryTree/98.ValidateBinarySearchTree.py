"""
https://leetcode.com/problems/validate-binary-search-tree/
Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""
import math

# [5,4,6,null,null,3,7] false
class Solution:
    def validate(self, node: Optional[TreeNode], low=-math.inf, high=math.inf) -> bool:
        if not node:
            return True
        if node.val <= low or node.val >= high:
            return False

        return self.validate(node.left, low, node.val) and self.validate(node.right, node.val, high)

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.validate(root)

"""
https://leetcode.com/problems/path-sum/
Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""
from collections import deque


def is_leaf(node: TreeNode):
    return not (node.left or node.right)


class Solution:
    """
    1. queue를 만든다.
    2. queue insert (node, sum)
    3. cond: leaf까지 간다. 이때 sum이 same이면 return True
    """

    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False

        queue = deque([(root, root.val)])  # node, sum
        while queue:
            node, partial_sum = queue.pop()
            if is_leaf(node) and partial_sum == targetSum:
                return True

            # insert
            if node.left:
                queue.appendleft((node.left, partial_sum + node.left.val))
            if node.right:
                queue.appendleft((node.right, partial_sum + node.right.val))

        return False

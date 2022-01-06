# https://leetcode.com/problems/minimum-depth-of-binary-tree/

"""
Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""

from collections import deque
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    @staticmethod
    def is_left_exist(node: TreeNode) -> bool:
        return True if node.left else False

    @staticmethod
    def is_right_exist(node: TreeNode) -> bool:
        return True if node.right else False

    @staticmethod
    def is_leaf_node(node: TreeNode) -> bool:
        return not (Solution.is_left_exist(node) or Solution.is_right_exist(node))

    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        queue = deque(
            [
                root,
            ]
        )

        cnt = 0
        while queue:

            n = len(queue)
            for _ in range(n):
                node = queue.popleft()
                if Solution.is_leaf_node(node):
                    return cnt + 1  # early return

                if Solution.is_left_exist(node):
                    queue.append(node.left)
                if Solution.is_right_exist(node):
                    queue.append(node.right)
            cnt += 1
        return -1

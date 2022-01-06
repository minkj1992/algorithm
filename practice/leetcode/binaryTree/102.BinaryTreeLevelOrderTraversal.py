"""
https://leetcode.com/problems/binary-tree-level-order-traversal/
Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""

from collections import deque


class Solution:
    """BFS
    1. initial root insert
    2. while queue && len(queue)는 level을 의미하니 빈 리스트를 만든다.
    3. pop 시점에 리스트에 append
    """

    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        result = []
        queue = deque([root])
        while queue:
            level_nodes = []
            n = len(queue)
            for _ in range(n):
                node = queue.pop()

                if node.left:
                    queue.appendleft(node.left)
                if node.right:
                    queue.appendleft(node.right)
                level_nodes.append(node.val)
            result.append(level_nodes)
        return result

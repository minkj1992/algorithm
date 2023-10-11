"""
https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/
Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""
from collections import deque


class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        is_reversed = False
        queue = deque([root])
        answer = []
        while queue:
            n = len(queue)
            level_nodes = []
            for _ in range(n):
                node = queue.pop()
                if node.left:
                    queue.appendleft(node.left)
                if node.right:
                    queue.appendleft(node.right)
                level_nodes.append(node.val)

            if is_reversed:
                level_nodes = reversed(level_nodes)
            is_reversed = not is_reversed

            answer.append(level_nodes)
        return answer

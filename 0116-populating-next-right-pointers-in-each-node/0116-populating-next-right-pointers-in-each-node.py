from collections import deque

"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""


class Solution:
    def connect(self, root: "Optional[Node]") -> "Optional[Node]":

        if not root:
            return root

        queue = deque([root])

        while queue:
            level = []
            length = len(queue)

            for index in range(length):
                node = queue.popleft()
                level.append(node)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

                if index > 0:
                    level[index - 1].next = level[index]
        return root

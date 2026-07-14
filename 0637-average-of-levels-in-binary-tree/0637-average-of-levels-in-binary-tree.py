from collections import deque


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:

        if not root:
            return [0]

        queue = deque([root])
        result = []

        while queue:
            level_length = len(queue)
            summation = 0
            for _ in range(level_length):
                node = queue.popleft()
                summation += node.val

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            result.append(summation / level_length)

        return result

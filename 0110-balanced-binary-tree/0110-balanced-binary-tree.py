'''
Time complexity - O(n^2) as the heights of the same subtrees are computed repeatedly
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        def height(root):
            if not root:
                return 0

            left_height = height(root.left)
            right_height = height(root.right)

            # print(
            #     f"Node {root.val}: left height = {left_height}, "
            #     f"right height = {right_height}"
            # )

            return 1 + max(left_height, right_height)

        if not root:
            return True
        left_height = height(root.left)
        right_height = height(root.right)

        # print(
        #     f"Checking node {root.val}: "
        #     f"left height = {left_height}, right height = {right_height}"
        # )

        return (
            abs(left_height - right_height) <= 1
            and self.isBalanced(root.left)
            and self.isBalanced(root.right)
        )

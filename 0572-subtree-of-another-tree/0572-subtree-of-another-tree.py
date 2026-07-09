"""
Time complexity - O(n*m)
n length of root tree m being length of subroot
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        def sameTree(root, subRoot):

            if root is None and subRoot is None:
                return True

            if root is None or subRoot is None:
                return False

            if root.val != subRoot.val:
                return False

            return sameTree(root.left, subRoot.left) and sameTree(
                root.right, subRoot.right
            )

        if root is None:
            return False

        if sameTree(root, subRoot):
            return True

        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

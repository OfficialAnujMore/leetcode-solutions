# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        def generatePreOrder(root, result):
            if root is None:
                result.append("#None")
                return result

            result.append("#" + str(root.val))
            generatePreOrder(root.left, result)
            generatePreOrder(root.right, result)

            return result

        rootPreOrder = generatePreOrder(root, [])
        subRootPreOrder = generatePreOrder(subRoot, [])

        rootStr = ",".join(rootPreOrder)
        subStr = ",".join(subRootPreOrder)

        return subStr in rootStr
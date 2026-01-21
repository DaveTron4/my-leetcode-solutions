# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        
        minDiff = [float('inf')]
        prev = [None]


        def helper(node):
            if not node:
                return

            helper(node.left)

            if prev[0] != None:
                diff = abs(node.val - prev[0])

                if diff < minDiff[0]:
                    minDiff[0] = diff

            prev[0] = node.val

            helper(node.right)

            return


        helper(root)

        return minDiff[0]
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        
        count = []
        sums = []

        def helper(node, depth):
            if not node:
                return 

            if depth == len(sums):
                sums.append(0)
                count.append(0)

            sums[depth] += node.val
            count[depth] += 1

            helper(node.left,  depth + 1)
            helper(node.right, depth + 1)

        helper(root, 0)

        result = []
        for i in range(len(sums)):
            result.append(sums[i] / count[i])

        return result
        
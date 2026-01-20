# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        '''
        U - 
            I - root of binary tree (root), interger target (targetSum)
            O - True if there is a path that adds up to targetSum, and fase if not
            C - None
            E - if no root return False
        P - 
            Go down a path and check if values add up to targetSum
            use helper function to traverse tree
            Substract from targetSum and if zero return True
        I - 
        '''
        
        def traverse(root, targetSum):
            if not root:
                return False
            if not root.left and not root.right:
                if root.val == targetSum:
                    return True
            targetSum -= root.val
            return traverse(root.left, targetSum) or traverse(root.right, targetSum)
            
        return traverse(root, targetSum)
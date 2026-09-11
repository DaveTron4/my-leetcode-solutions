# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: TreeNode) -> int:
        if root.left == None and root.right == None and root.val != None:
            return 1

        matching_nodes_count = 0 

        def calculate_subtree(node):
            nonlocal matching_nodes_count 

            if not node:
                return 0, 0

            left_sum, left_count = calculate_subtree(node.left)
            right_sum, right_count = calculate_subtree(node.right)
            
            total_sum = node.val + left_sum + right_sum
            total_count = 1 + left_count + right_count
            
            current_average = total_sum // total_count
            
            if current_average == node.val:
                matching_nodes_count += 1

            return total_sum, total_count
 
        calculate_subtree(root)
        
        return matching_nodes_count
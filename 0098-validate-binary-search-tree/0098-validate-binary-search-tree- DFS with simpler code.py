# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # Simpler DFS
        def dfs(root, left_range, right_range):
            if root:
                if root.val <= left_range or root.val >= right_range:
                    return False
                return dfs(root.left, left_range, root.val) and dfs(root.right, root.val, right_range)
            return True
        return dfs(root, -inf, inf)
            



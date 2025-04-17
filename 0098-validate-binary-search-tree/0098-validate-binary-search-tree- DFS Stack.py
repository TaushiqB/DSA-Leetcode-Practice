# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # Depth First Search(Stack, Similar to BFS(level order) but POP instead of Popleft()) and Assigning Range

        def dfs(root):
            if not root:
                return True
            stack = [(root, float(-inf), float(inf))]

            while stack:
                node, left_range, right_range = stack.pop()
                print(node.val)
                if not (left_range < node.val < right_range):
                    return False

                if node.right:
                    stack.append((node.right, node.val, right_range))

                if node.left:
                    stack.append((node.left, left_range, node.val))
            return True
        return dfs(root)
            



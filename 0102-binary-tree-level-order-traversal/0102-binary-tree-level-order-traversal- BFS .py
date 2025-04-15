# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # Level order Breadth first search
        def bfs(root):
            c = 0
            level_nodes = []
            if not root:
                return 
            queue = deque([(root, 0)])
            while queue:
                node, l = queue.popleft()
                if c!=l:
                    ans.append(level_nodes)
                    level_nodes = []
                    c = l
                if node:
                    level_nodes.append(node.val)
                    queue.append((node.left, l+1))
                    queue.append((node.right, l+1))

        ans = []
        bfs(root)
        return ans
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        # Double DFS Solution
        parents = {}
        # First DFS
        def dfs(root, parent):
            if not root:
                return 
            parents[root] = parent
            dfs(root.left, root)
            dfs(root.right, root)

        # Second DFS
        def dist(root, c):
            if not root or root in seen or c > k:
                return
            if c == k:
                res.append(root.val)
            seen.add(root)
            dist(root.left, c+1)
            dist(root.right, c+1)
            dist(parents[root], c+1)

        dfs(root, None)
        c = 0
        res = []
        seen = set()
        dist(target, c)
        return res
        
        

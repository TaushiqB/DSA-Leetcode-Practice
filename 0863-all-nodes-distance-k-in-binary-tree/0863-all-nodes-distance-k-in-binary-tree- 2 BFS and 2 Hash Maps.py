# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        # Double BFS and Double Hash maps Solution
        parents = {}
        # Level Order Traversal: First BFS, also store the parents in hashmaps
        def bfs(root):
            if not root:
                return 
            queue = deque([root])
            while queue:
                node = queue.popleft()

                if node.left:
                    queue.append(node.left)
                    parents[node.left] = node
                if node.right:
                    queue.append(node.right)
                    parents[node.right] = node
        bfs(root)
        #Second BFS Traversal
        queue = deque([target])
        curr_level = 0
        seen = {target}
        while queue:
            print([node.val for node in queue])
            if curr_level == k:
                break
            curr_level += 1

            for i in range(len(queue)):
                node = queue.popleft()

                if node.left and node.left not in seen:
                    queue.append(node.left)
                    seen.add(node.left)
                if node.right and node.right not in seen:
                    queue.append(node.right)
                    seen.add(node.right)
                if node in parents and parents[node] not in seen:
                    queue.append(parents[node])
                    seen.add(parents[node])

        return [node.val for node in queue]

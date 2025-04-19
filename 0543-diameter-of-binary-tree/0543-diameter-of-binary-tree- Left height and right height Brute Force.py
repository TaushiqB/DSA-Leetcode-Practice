# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # Brute Force Solution O(n^2)
    # Consider each Node as root and calculate the sum of its left and right height and find the max out of all of them
    # Helper function to compute the height of a subtree
    def height(self, node):
        if not node:
            return 0
        return 1 + max(self.height(node.left), self.height(node.right))

    # Main function to compute the diameter
    def diameterOfBinaryTree(self, root):
        if not root:
            return 0

        # Height of left and right subtrees
        left_height = self.height(root.left)
        right_height = self.height(root.right)

        # Diameter passing through current node
        current_diameter = left_height + right_height

        # Diameter in left and right subtrees
        left_diameter = self.diameterOfBinaryTree(root.left)
        right_diameter = self.diameterOfBinaryTree(root.right)

        # Return the maximum diameter
        return max(current_diameter, right_diameter, left_diameter)
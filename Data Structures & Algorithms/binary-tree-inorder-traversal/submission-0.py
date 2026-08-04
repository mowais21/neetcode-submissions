# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # visit the root node, traverse the left subtree, traverse the right subtree
        visited = []
        self.traverse(root, visited)
        return visited

    def traverse(self, root, visited):
        if root is None:
            return
        
        self.traverse(root.left, visited)
        visited.append(root.val)
        self.traverse(root.right, visited)
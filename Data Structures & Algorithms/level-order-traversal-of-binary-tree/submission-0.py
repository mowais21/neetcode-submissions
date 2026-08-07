# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

# deque.popleft()
# deque.append()

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []

        queue = deque()
        queue.append(root)

        while queue:
            nodesinlevel = len(queue)
            curlevel = []

            for i in range(nodesinlevel):
                node = queue.popleft()
                if node:
                    curlevel.append(node.val)
                    queue.append(node.left)
                    queue.append(node.right)
            if curlevel:
                res.append(curlevel)

        return res
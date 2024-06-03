# 102. Binary Tree Level Order Traversal
# Medium
# Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).

# Example 1:

# Input: root = [3,9,20,null,null,15,7]
# Output: [[3],[9,20],[15,7]]

from collections import deque

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        queue = deque()

        if root:
            queue.append(root)

        level = 0
        # Complete list of all the levels - List Order Traversal
        lot = []
        while len(queue) > 0:
            traversal_level = []
            for i in range(len(queue)):
                curr = queue.popleft()
                traversal_level.append(curr.val)
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
            lot.append(traversal_level)
            level += 1

        return lot
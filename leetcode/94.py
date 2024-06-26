# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def inorderTraversal(self, root):
        res = []
        self.helper(root,res)
        return res

    def helper(self, root, res):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return     
        self.helper(root.left, res)
        res.append(root.val)
        self.helper(root.right, res)
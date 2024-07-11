def inorderTraversal(root):
    """
    :type root: TreeNode
    :rtype: List[int]
    """
    def dfs(root, arr):
        """
        dfs = Depth First Search - Iterate all the way to the bottom of the tree and then back up 
        
        Remember process and append order - Inorder traversal
        1. Left 
        2. Root
        3. Right
        """
        if not root:
            return 
        
        # left
        dfs(root.left, arr)
        # root
        arr.append(root.val)
        # right
        dfs(root.right, arr)

        return arr

    return dfs(root, [])


def dfs(root, arr):
    """
    Remember process and append order - Preorder traversal (root first)
    1. Root 
    2. Left
    3. Right
    """
    if not root:
        return 
    # root
    arr.append(root.val)
    # left
    dfs(root.left, arr)
    # right
    dfs(root.right, arr)

    return arr
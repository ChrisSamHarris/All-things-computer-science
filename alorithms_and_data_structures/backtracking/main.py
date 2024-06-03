class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

#### Reach Leaf - Return Bool ####

def canReachLeaf(root):
    if not root or root.val == 0:
		# retun false if we can not get to a path we're looking for 
        return False
    
    if not root.left and not root.right:
        return True
    if canReachLeaf(root.left):
        return True
    if canReachLeaf(root.right):
        return True
    return False

#### Reach Leaf - Return Path ####

def leafPath(root, path):
    if not root or root.val == 0:
        return False
    path.append(root.val)

    if not root.left and not root.right:
        return True
    if leafPath(root.left, path):
        return True
    if leafPath(root.right, path):
        return True
    path.pop()
    return False
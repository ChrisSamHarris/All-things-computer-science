from collections import deque

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
    
def insert_into_bst(root, val):
    if root is None:
        return TreeNode(val)
    if val < root.val:
        root.left = insert_into_bst(root.left, val)
    else:
        root.right = insert_into_bst(root.right, val)
    return root

def create_tree(values):
    if not values:
        return None
    root = TreeNode(values[0])
    for val in values[1:]:
        insert_into_bst(root, val)
    return root

# Values to create the tree with
values = [4, 2, 7, 1, 3]
tree = create_tree(values)

# Helper function to print the tree (in-order traversal)
def print_tree(root):
    if root:
        print_tree(root.left)
        print(root.val, end=' ')
        print_tree(root.right)

print_tree(tree)

        
#### BINARY SEARCH TREE 

def search(root, target):
    if not root:
        return False
    
    if target > root.val:
        return search(root.right, target)
    elif target < root.val:
        return search(root.left, target)
    else:
        return True
    
    
#### Binary Search Tree #### 
class Solution(object):
    def searchBST(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        if not root:
            return None

        if val > root.val:
            return self.searchBST(root.right, val)
        elif val < root.val:
            return self.searchBST(root.left, val)
        else:
            return root
        
Solution().searchBST(TreeNode([4,2,7,1,3]), 2)


#### BST - Insert/ Remove ####

# Insert a new node and return the root of the BST.
def insert(root, val):
    if not root:
        return TreeNode(val)
    
    if val > root.val:
        root.right = insert(root.right, val)
    elif val < root.val:
        root.left = insert(root.left, val)
    return root

# Return the minimum value node of the BST.
def minValueNode(root):
    curr = root
    while curr and curr.left:
        curr = curr.left
    return curr

# Remove a node and return the root of the BST.
def remove(root, val):
    if not root:
        return None
    
    if val > root.val:
        root.right = remove(root.right, val)
    elif val < root.val:
        root.left = remove(root.left, val)
    else:
        if not root.left:
            return root.right
        elif not root.right:
            return root.left
        else:
            minNode = minValueNode(root.right)
            root.val = minNode.val
            root.right = remove(root.right, minNode.val)
    return root

#### BST Traversal ####

def inorder(root):
    """
    """
    if not root:
        return    
    inorder(root.left)
    print(root.val)
    inorder(root.right)
    
def preorder(root):
    """
    """
    if not root:
        return    
    print(root.val)
    preorder(root.left)
    preorder(root.right)
    
def postorder(root):
    """
    """
    if not root:
        return    
    postorder(root.left)
    postorder(root.right)
    print(root.val)


#### BREADTH FIRST SEARCH (BFS) ####

def bfs(root):
    queue = deque()

    if root:
        queue.append(root)
    
    level = 0
    while len(queue) > 0:
        print("level: ", level)
        for i in range(len(queue)):
            curr = queue.popleft()
            print(curr.val)
            if curr.left:
                queue.append(curr.left)
            if curr.right:
                queue.append(curr.right)
        level += 1
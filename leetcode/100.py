from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def isSameTree(p: TreeNode, q: TreeNode) -> bool:
    def check(n1, n2):
        if not n1 and not n2:
            return True
        if not n1 or not n2:
            return False
        return n1.val == n2.val

    deq = deque([(p, q)])
    
    while deq:
        n1, n2 = deq.popleft()
        
        if not check(n1, n2):
            return False
        
        if n1:
            deq.append((n1.left, n2.left))
            deq.append((n1.right, n2.right))
    
    return True

# Example usage:
p = TreeNode(1, TreeNode(2), TreeNode(3))
q = TreeNode(1, TreeNode(2), TreeNode(3))
print(isSameTree(p, q))  # Output: true


### Recursive 

class Solution(object):
    def isSameTree(self, p, q):
        """
        Recursive check
        """;
        # base case(s)
        if not p and not q:
            return True 
        if not p or not q:
            return False 
        if p.val != q.val:
            return False 

        # recursive case to iterate through the tree
        return self.isSameTree(p.left,q.left) and self.isSameTree(p.right,q.right)
class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None

class MyLinkedList(object):
    def __init__(self):
        self.left = ListNode(0)
        self.right = ListNode(0)
        self.left.next = self.right
        self.right.prev = self.left 

    def get(self, index):
        """
        :type index: int
        :rtype: int
        """
        cur = self.left.next
        while cur and index > 0:
            cur = cur.next
            index -= 1
        if cur and cur != self.right and index == 0:
            return cur.val
        return -1 

    def addAtHead(self, val):
        """
        :type val: int
        :rtype: None
        """
        self.addNode(val, self.left.next, self.left)
        

    def addAtTail(self, val):
        """
        :type val: int
        :rtype: None
        """
        self.addNode(val, self.right, self.right.prev)

    def addNode(self, val, nxt_node, prev_node):
        node, nxt, prev = ListNode(val), nxt_node, prev_node
        prev.next = node 
        nxt.prev = node 
        node.next = nxt 
        node.prev = prev 


    def addAtIndex(self, index, val):
        """
        :type index: int
        :type val: int
        :rtype: None
        """
        cur = self.left.next 
        while cur and index > 0:
            cur = cur.next
            index -= 1 
        if cur and index == 0:
            self.addNode(val, cur, cur.prev)
        

    def deleteAtIndex(self, index):
        """
        :type index: int
        :rtype: None
        """
        cur = self.left.next 
        while cur and index > 0:
            cur = cur.next
            index -= 1 
        if cur and cur != self.right and index ==0:
            nxt, prev = cur.next, cur.prev 
            nxt.prev = prev 
            prev.next = nxt
        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)
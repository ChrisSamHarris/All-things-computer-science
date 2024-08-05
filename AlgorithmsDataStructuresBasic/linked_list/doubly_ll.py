class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None
        
listNode1 = ListNode(1)
listNode2 = ListNode(2)
listNode3 = ListNode(3)

listNode1.next = listNode2
listNode2.next = listNode3
listNode3.next = None

listNode1.prev = None
listNode2.prev = listNode1
listNode3.prev = listNode2

tail = listNode3
print(tail.val)

listNode4 = ListNode(4)
listNode3.next = listNode4
tail = tail.next
print(tail.val)

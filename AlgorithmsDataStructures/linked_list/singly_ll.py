class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None
        
listNode1 = ListNode(1)
listNode2 = ListNode(2)
listNode3 = ListNode(3)

listNode1.next = listNode2
listNode2.next = listNode3
listNode3.next = None
    
cur = listNode1
while cur:
    print(cur.val)
    cur = cur.next
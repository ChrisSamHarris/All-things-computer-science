class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

#### Find the middle of a linked list using fast and slow pointers ####
def middleOfList(head):
    slow, fast = head, head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow

#### Q: Determine if a Linked List has a cycle ####
# original method O(n) time and space
def hasCycle(head: ListNode) -> bool:
    visited = set()
    while head is not None:
        if head in visited:
            return True
        visited.add(head)
        head = head.next
        
    return False

# fast and slow pointers O(n) time and O(1) space
def hasCycle(head):
    slow, fast = head, head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False

#### ***Q: Determine if a Linked List has a cycle and return the head of the cycle*** ####
def cycleStart(head):
    slow, fast = head, head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            break

    if not fast or not fast.next:
        return None
    
	# Logic added to return the head of the cycle
    slow2 = head
    while slow != slow2:
        slow = slow.next
        slow2 = slow2.next
    return slow
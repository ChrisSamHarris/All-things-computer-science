### LINKED LIST 

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
def traversing_ll(head):
    cur = head #ListNode1
    while cur:
        cur = cur.next


# Creating nodes
node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)
node5 = Node(5)

# Linking nodes
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5

# Function to print the linked list
def print_linked_list(head):
    current_node = head
    while current_node:
        print(current_node.data, end=" -> ")
        current_node = current_node.next
    print("None")

# Printing the linked list starting from node1
print_linked_list(node1)

### DOUBLY LINKED LIST 
# addition
tail.next = Node4
Node4.prev = tail
tail = tail.next

#deletion
ListNode2 = tail.prev
ListNode2.next = null
tail = ListNode2




### QUEUE - FIFO

# Add to a queue 
def enqueue(self, val):
    newNode = Node(val)

    # Queue is non-empty
    if self.right:
        self.right.next = newNode
        self.right = self.right.next
    # Queue is empty
    else:
        self.left = self.right = newNode
        
# Remove from a queue
def dequeue(self):
    # Queue is empty
    if not self.left:
        return None
    
    # Remove left node and return value
    val = self.left.val
    self.left = self.left.next
    if not self.left:
        self.right = None
    return val

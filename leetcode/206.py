class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

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
        
def reverseList(head):
    """
    :type head: ListNode
    :rtype: ListNode
    """
    prev, curr = None, head 

    while curr: 
        nxt = curr.next
        curr.next = prev
        prev = curr 
        curr = nxt 
    return prev

rev_link = reverseList(node1)
print_linked_list(rev_link)



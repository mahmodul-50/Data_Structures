class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

def insert_at_head(head, val):
    newnode = Node(val)
    newnode.next = head
    head = newnode
    return head

def print_linked_list(head):
    tmp = head
    while tmp != None:
        print(tmp.val)
        tmp = tmp.next

head = None

head = insert_at_head(head, 10)
head = insert_at_head(head, 20)
head = insert_at_head(head, 30)
head = insert_at_head(head, 40)

print_linked_list(head)
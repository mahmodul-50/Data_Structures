class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

def insert_at_tail(head, tail, val):
    newnode = Node(val)
    if head is None:
        head = newnode
        tail = newnode
        return head, tail
    tmp = head
    while tmp.next is not None:
        tmp = tmp.next
    tmp.next = newnode
    return head, tail

def printing(head):
    tmp = head
    while tmp is not None:
        print(tmp.val, end="  ")
        tmp = tmp.next
    print()

head = None
tail = None

head, tail = insert_at_tail(head, tail, 40)
head, tail = insert_at_tail(head, tail, 50)
head, tail = insert_at_tail(head, tail, 60)

printing(head)

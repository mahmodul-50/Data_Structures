class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

def insert_at_tail(head, val):
    newnode = Node(val)
    if head == None:
        head = newnode
        return head
    tmp = head
    while tmp.next != None:
        tmp = tmp.next
    tmp.next =newnode
    return head

def printing(head):
    tmp = head
    while tmp is not None:
        print(tmp.val, end="  ")
        tmp = tmp.next
    print()

head = None

head = insert_at_tail(head, 40)
head = insert_at_tail(head, 50)
head = insert_at_tail(head, 60)

printing(head)
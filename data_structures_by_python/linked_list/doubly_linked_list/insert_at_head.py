class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None


def print_forward(head):
    tmp = head
    while tmp is not None:
        print(tmp.val, end=" ")
        tmp = tmp.next
    print()


def insert_at_head(val):
    global head, tail
    newnode = Node(val)

    if head is None:
        head = newnode
        tail = newnode
        return

    newnode.next = head
    head.prev = newnode
    head = newnode


head = Node(10)
a = Node(20)
tail = Node(30)

head.next = a
a.prev = head

a.next = tail
tail.prev = a

insert_at_head(100)
insert_at_head(200)

print_forward(head)

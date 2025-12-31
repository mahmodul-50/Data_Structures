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


def insert_at_any_pos(head, idx, val):
    newnode = Node(val)
    tmp = head

    for i in range(1, idx):
        tmp = tmp.next

    newnode.next = tmp.next
    tmp.next.prev = newnode
    tmp.next = newnode
    newnode.prev = tmp


head = Node(10)
a = Node(20)
tail = Node(30)

head.next = a
a.prev = head
a.next = tail
tail.prev = a

insert_at_any_pos(head, 2, 100)
insert_at_any_pos(head, 1, 500)
print_forward(head)

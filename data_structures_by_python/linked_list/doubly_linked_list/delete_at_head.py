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


def delete_at_head():
    global head, tail
    if head is None:
        return
    deleteNode = head
    head = head.next
    if head is None:
        tail = None
        return
    head.prev = None


head = Node(10)
a = Node(20)
tail = Node(30)

head.next = a
a.prev = head
a.next = tail
tail.prev = a

delete_at_head()
delete_at_head()

print_forward(head)

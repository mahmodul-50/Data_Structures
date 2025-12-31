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


def delete_at_tail():
    global head, tail
    if tail is None:
        return
    deleteNode = tail
    tail = tail.prev
    if tail is None:
        head = None
        return
    tail.next = None


head = Node(10)
a = Node(20)
tail = Node(30)

head.next = a
a.prev = head
a.next = tail
tail.prev = a

delete_at_tail()
print_forward(head)

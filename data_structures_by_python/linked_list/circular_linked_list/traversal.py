class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


def traversal(head):
    if head is None:
        return
    tmp = head
    while True:
        print(tmp.val, end=" ")
        tmp = tmp.next
        if tmp == head:
            break
    print()


head = Node(10)
a = Node(20)
b = Node(30)
c = Node(40)

head.next = a
a.next = b
b.next = c
c.next = head

traversal(head)

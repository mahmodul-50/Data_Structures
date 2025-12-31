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


def insert_at_tail(val):
    global head, tail
    newnode = Node(val)
    if head is None:
        head = newnode
        tail = newnode
        return
    tail.next = newnode
    newnode.prev = tail
    tail = newnode


head = None
tail = None
while True:
    val = int(input())
    if val == -1:
        break
    insert_at_tail(val)
print_forward(head)

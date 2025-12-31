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
    tail.next = newnode
    tail = newnode
    return head, tail


def print_linked_list(head):
    tmp = head
    while tmp is not None:
        print(tmp.val)
        tmp = tmp.next


def print_reverse(tmp):
    if tmp is None:
        return
    print_reverse(tmp.next)
    print(tmp.val)


head = None
tail = None
while True:
    val = int(input())
    if val == -1:
        break
    head, tail = insert_at_tail(head, tail, val)
print_reverse(head)

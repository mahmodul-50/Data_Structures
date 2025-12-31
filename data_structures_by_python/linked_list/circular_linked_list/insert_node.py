class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


def insert_node(val):
    global head
    newnode = Node(val)
    if head is None:
        head = newnode
        newnode.next = head
        return
    tmp = head
    while tmp.next != head:
        tmp = tmp.next
    tmp.next = newnode
    newnode.next = head


def traversal():
    if head is None:
        return
    tmp = head
    while True:
        print(tmp.val, end=" ")
        tmp = tmp.next
        if tmp == head:
            break
    print()


head = None

insert_node(10)
insert_node(20)
insert_node(30)
insert_node(40)

traversal()

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

def printing(head):
    tmp = head
    # while tmp is not None:
    while tmp != None:
        print(tmp.val, end="  ")
        tmp = tmp.next
    print()

head = Node(10)
a = Node(20)
b = Node(30)

head.next = a
a.next = b

printing(head)
class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


def detect_cycle(head):
    slow = head
    fast = head
    flag = False
    while fast != None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            flag = True
            break
    if flag == True:
        print("Cycle Detected")
    else:
        print("No Cycle")


head = Node(10)
a = Node(20)
b = Node(30)
c = Node(40)
d = Node(50)

head.next = a
a.next = b
b.next = c
c.next = d
d.next = d

detect_cycle(head)

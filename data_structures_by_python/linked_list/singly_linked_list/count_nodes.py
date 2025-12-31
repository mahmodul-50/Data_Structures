class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


def count_node(head):
    tmp = head
    cnt = 0
    while tmp != None:
        cnt += 1
        tmp = tmp.next
    return cnt


head = Node(10)
a = Node(20)
b = Node(30)

head.next = a
a.next = b

print(count_node(head))
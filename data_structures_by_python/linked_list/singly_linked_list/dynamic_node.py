class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


head = Node(10)
a = Node(20)
b = Node(30)

head.next = a
a.next = b

print(head.val)
print(head.next.val)
print(head.next.next.val)

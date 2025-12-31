class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


head = Node(10)
a = Node(20)
b = Node(30)

head.next = a
a.next = b
b.next = head

tmp = head
for i in range(3):
    print(tmp.val, end=" ")
    tmp = tmp.next
print()

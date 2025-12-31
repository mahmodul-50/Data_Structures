class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


a = Node(10)
b = Node(20)
c = Node(30)
a.next = b
b.next = c

print(a.val)
print(a.next.val)
print(a.next.next.val)

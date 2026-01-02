class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None



root = Node(10)
a = Node(20)
b = Node(30)
c = Node(40)
d = Node(50)
e = Node(60)

root.left = a
root.right = b
a.left = c
b.left = d
b.right = e

print("Root:", root.val)
print("Root left:", root.left.val)
print("Root right:", root.right.val)
print("b children:", b.left.val, b.right.val)
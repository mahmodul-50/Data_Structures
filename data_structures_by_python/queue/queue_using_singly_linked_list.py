class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


class my_queue:
    def __init__(self):
        self.head = None
        self.tail = None
        self.sz = 0

    def push(self, val):  # O(1)
        self.sz += 1
        newnode = Node(val)
        if self.head is None:
            self.head = newnode
            self.tail = newnode
            return
        self.tail.next = newnode
        self.tail = newnode

    def pop(self):  # O(1)
        if self.head is None:
            return
        self.sz -= 1
        deleteNode = self.head
        self.head = self.head.next
        if self.head is None:
            self.tail = None

    def front(self):  # O(1)
        return self.head.val

    def size(self):
        return self.sz

    def empty(self):
        return self.head is None


q = my_queue()

n = int(input())
for _ in range(n):
    val = int(input())
    q.push(val)

while not q.empty():
    print(q.front(), end=" ")
    q.pop()

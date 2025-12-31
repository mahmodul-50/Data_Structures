class MyQueue:
    def __init__(self):
        self.l = []

    def push(self, val):  # O(1) amortized
        self.l.append(val)

    def pop(self):  # O(n) in list
        self.l.pop(0)

    def front(self):  # O(1)
        return self.l[0]

    def back(self):  # O(1)
        return self.l[-1]

    def size(self):  # O(1)
        return len(self.l)

    def empty(self):  # O(1)
        return len(self.l) == 0


q = MyQueue()

n = int(input())
for i in range(n):
    val = int(input())
    q.push(val)

while not q.empty():
    print(q.front(), end=" ")
    q.pop()

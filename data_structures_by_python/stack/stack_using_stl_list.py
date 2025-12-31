class my_stack:
    def __init__(self):
        self.l = []

    def push(self, val):
        self.l.append(val)

    def pop(self):
        self.l.pop()

    def top(self):
        return self.l[-1]

    def size(self):
        return len(self.l)

    def empty(self):
        return len(self.l) == 0


st = my_stack()

n = int(input())
for _ in range(n):
    x = int(input())
    st.push(x)

while not st.empty():
    print(st.top(), end=" ")
    st.pop()

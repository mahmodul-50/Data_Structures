class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


class my_stack:
    def __init__(self):
        self.head = None
        self.sz = 0

    def push(self, val):  # O(1)
        self.sz += 1
        newnode = Node(val)
        newnode.next = self.head
        self.head = newnode

    def pop(self):  # O(1)
        if self.head is None:
            return
        self.sz -= 1
        self.head = self.head.next

    def top(self):  # O(1)
        return self.head.val

    def size(self):  # O(1)
        return self.sz

    def empty(self):  # O(1)
        return self.head is None


st = my_stack()

st.push(10)
st.push(20)
st.push(30)
st.push(40)

print(st.top())

while not st.empty():
    print(st.top(), end=" ")
    st.pop()

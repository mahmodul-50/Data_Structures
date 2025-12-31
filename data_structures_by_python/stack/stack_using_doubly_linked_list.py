class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None


class my_stack:
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
        newnode.prev = self.tail
        self.tail = newnode

    def pop(self):  # O(1)
        if self.tail is None:
            return
        self.sz -= 1
        deletenode = self.tail
        self.tail = self.tail.prev
        if self.tail is None:
            self.head = None
            return
        self.tail.next = None

    def top(self):  # O(1)
        return self.tail.val

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

class my_stack:
    def __init__(self):
        self.v = []

    def push(self, val):
        self.v.append(val)

    def pop(self):
        self.v.pop()

    def top(self):
        return self.v[-1]

    def size(self):
        return len(self.v)

    def empty(self):
        return len(self.v) == 0


st = my_stack()
st.push(29)
st.push(48)
st.push(49)

print(st.top())
class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


def insert_at_tail(head, tail, val):
    newnode = Node(val)
    if head is None:
        head = newnode
        tail = newnode
        return head, tail
    tail.next = newnode
    tail = newnode
    return head, tail

def delete_at_head(head):
    if head is None:
        return None
    delete_node = head
    head = head.next
    del delete_node
    return head

def print_linked_list(head):
    tmp = head
    while tmp is not None:
        print(tmp.val, end=" ")
        tmp = tmp.next
    print()


head = None
tail = None
while True:
    val = int(input())
    if val == -1:
        break
    head, tail = insert_at_tail(head, tail, val)

head = delete_at_head(head)
print_linked_list(head)

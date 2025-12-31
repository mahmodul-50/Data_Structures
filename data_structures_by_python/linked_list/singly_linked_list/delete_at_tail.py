class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

def insert_at_tail(head, tail, val):
    new_node = Node(val)
    if head is None:
        head = new_node
        tail = new_node
        return head, tail
    tail.next = new_node
    tail = new_node
    return head, tail

def delete_at_tail(head, tail):
    if head is None:
        return head, tail
    if head.next is None:
        head = None
        tail = None
        return head, tail
    temp = head
    while temp.next.next is not None:
        temp = temp.next
    temp.next = None
    tail = temp
    return head, tail

def print_linked_list(head):
    temp = head
    while temp is not None:
        print(temp.val, end=" ")
        temp = temp.next
    print()

head = None
tail = None
head, tail = insert_at_tail(head, tail, 10)
head, tail = insert_at_tail(head, tail, 20)
head, tail = insert_at_tail(head, tail, 30)
head, tail = insert_at_tail(head, tail, 40)

print_linked_list(head)
print("Tail before delete:", tail.val)

head, tail = delete_at_tail(head, tail)

print_linked_list(head)
print("Tail after delete:", tail.val)
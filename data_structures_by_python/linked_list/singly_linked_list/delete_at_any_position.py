class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


def delete_at_any_pos(head, idx):
    tmp = head
    for _ in range(1, idx):
        tmp = tmp.next
    delete_node = tmp.next
    tmp.next = delete_node.next
    del delete_node


def print_linked_list(head):
    tmp = head
    while tmp is not None:
        print(tmp.val, end=" ")
        tmp = tmp.next
    print()


head = Node(10)
a = Node(20)
tail = Node(30)
head.next = a
a.next = tail
delete_at_any_pos(head, 2)
print_linked_list(head)

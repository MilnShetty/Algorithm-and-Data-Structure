class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def split_linked_list(head):
    if not head:
        return None, None

    slow_ptr = head
    fast_ptr = head
    prev_slow_ptr = None

    while fast_ptr is not None and fast_ptr.next is not None:
        fast_ptr = fast_ptr.next.next
        prev_slow_ptr = slow_ptr
        slow_ptr = slow_ptr.next

    if prev_slow_ptr is not None:
        prev_slow_ptr.next = None

    return head, slow_ptr

def print_linked_list(head):
    current = head
    while current:
        print(current.val, end=" -> ")
        current = current.next
    print("None")


A = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))


B, C = split_linked_list(A)


print("Linked List B:")
print_linked_list(B)

print("Linked List C:")
print_linked_list(C)

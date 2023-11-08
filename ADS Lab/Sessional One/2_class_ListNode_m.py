class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def merge_sorted_lists(A, B):
    dummy = ListNode()
    current = dummy

    while A is not None and B is not None:
        if A.val < B.val:
            current.next = A
            A = A.next
        else:
            current.next = B
            B = B.next
        current = current.next

    if A is not None:
        current.next = A
    else:
        current.next = B

    return dummy.next

def print_linked_list(head):
    current = head
    while current:
        print(current.val, end=" -> ")
        current = current.next
    print("None")

A = ListNode(1, ListNode(3, ListNode(5)))
B = ListNode(2, ListNode(4, ListNode(6)))

C = merge_sorted_lists(A, B)

print_linked_list(C)

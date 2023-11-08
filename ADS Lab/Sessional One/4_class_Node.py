class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.count = 0

class HeadStructure:
    def __init__(self):
        self.head_ptr = None
        self.num = 0

def insert_at_end(head_structure, data):
    new_node = Node(data)
    if head_structure.head_ptr is None:
        head_structure.head_ptr = new_node
    else:
        current = head_structure.head_ptr
        while current.next:
            current = current.next
        current.next = new_node
    head_structure.num += 1

def delete_node(head_structure, data):
    if head_structure.head_ptr is None:
        print("Linked list is empty.")
        return

    if head_structure.head_ptr.data == data:
        head_structure.head_ptr = head_structure.head_ptr.next
        head_structure.num -= 1
        return

    current = head_structure.head_ptr
    prev = None

    while current is not None:
        if current.data == data:
            prev.next = current.next
            head_structure.num -= 1
            return
        prev = current
        current = current.next

    print("Data not found in the linked list.")

def print_linked_list(head_structure):
    current = head_structure.head_ptr
    while current:
        print(current.data, end=" -> ")
        current = current.next
    print("None")


head_struct = HeadStructure()


insert_at_end(head_struct, 1)
insert_at_end(head_struct, 2)
insert_at_end(head_struct, 3)


print_linked_list(head_struct)
print("Number of elements:", head_struct.num)


delete_node(head_struct, 2)


print_linked_list(head_struct)
print("Number of elements:", head_struct.num)

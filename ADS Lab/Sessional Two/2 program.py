from collections import deque

class TreeNode:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

def insert(root, key):
    if root is None:
        return TreeNode(key)
    else:
        if key < root.val:
            root.left = insert(root.left, key)
        else:
            root.right = insert(root.right, key)
    return root

def minValueNode(node):
    current = node
    while current.left is not None:
        current = current.left
    return current

def deleteNode(root, key):
    if root is None:
        return root

    if key < root.val:
        root.left = deleteNode(root.left, key)
    elif key > root.val:
        root.right = deleteNode(root.right, key)
    else:
        if root.left is None:
            return root.right
        elif root.right is None:
            return root.left
        root.val = minValueNode(root.right).val
        root.right = deleteNode(root.right, root.val)
    return root

def level_order_traversal(root):
    if root is None:
        return
    queue = deque()
    queue.append(root)
    while queue:
        node = queue.popleft()
        print(node.val, end=' ')
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)

# Creating a sample binary search tree
root = None
keys = [50, 30, 70, 20, 40, 60, 80]

for key in keys:
    root = insert(root, key)

print("Level Order Traversal:")
level_order_traversal(root)

# Deleting a node (e.g., key 30)
key_to_delete = 30
root = deleteNode(root, key_to_delete)

print("\nLevel Order Traversal after deleting", key_to_delete)
level_order_traversal(root)

class TreeNode:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

def count_leaf_nodes(root):
    if root is None:
        return 0
    if root.left is None and root.right is None:
        return 1
    left_leaves = count_leaf_nodes(root.left)
    right_leaves = count_leaf_nodes(root.right)
    return left_leaves + right_leaves

def count_total_nodes(root):
    if root is None:
        return 0
    left_nodes = count_total_nodes(root.left)
    right_nodes = count_total_nodes(root.right)
    return 1 + left_nodes + right_nodes

def display_all_values(root):
    if root is not None:
        display_all_values(root.left)
        print(root.val, end=' ')
        display_all_values(root.right)

# Creating a sample binary tree
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)

# a. Count the number of leaf nodes
leaf_count = count_leaf_nodes(root)
print(f"Number of leaf nodes: {leaf_count}")

# b. Count the total number of nodes
total_nodes = count_total_nodes(root)
print(f"Total number of nodes: {total_nodes}")

# c. Display all the values of the nodes
print("Values of all nodes:")
display_all_values(root)

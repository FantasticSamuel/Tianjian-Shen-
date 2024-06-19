import random
import string

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def parse_tree(s):
    if s == '*':
        return None
    if '(' not in s:
        return TreeNode(s)

    # Find the root value and the subtrees
    root_value = s[0]
    subtrees = s[2:-1]  # Remove the root and the outer parentheses

    # Use a stack to find the comma that separates the left and right subtrees
    stack = []
    comma_index = None
    for i, char in enumerate(subtrees):
        if char == '(':
            stack.append(char)
        elif char == ')':
            stack.pop()
        elif char == ',' and not stack:
            comma_index = i
            break

    left_subtree = subtrees[:comma_index] if comma_index is not None else subtrees
    right_subtree = subtrees[comma_index + 1:] if comma_index is not None else None

    # Parse the subtrees
    root = TreeNode(root_value)
    root.left = parse_tree(left_subtree)
    root.right = parse_tree(right_subtree) if right_subtree else None
    return root


# Define the traversal functions
def preorder_traversal(root):
    if root is None:
        return ""
    return root.value + preorder_traversal(root.left) + preorder_traversal(root.right)


def inorder_traversal(root):
    if root is None:
        return ""
    return inorder_traversal(root.left) + root.value + inorder_traversal(root.right)

def generate_random_tree(depth=3):
    if depth == 0 or random.random() > 0.7:  # base case and random end condition
        return None

    node = TreeNode(random.choice(string.ascii_uppercase))
    node.left = generate_random_tree(depth - 1)
    node.right = generate_random_tree(depth - 1)
    return node


def encode_tree_to_string(node):
    if not node:
        return "*"

    if not node.left and not node.right:
        return node.value

    left_subtree = encode_tree_to_string(node.left) if node.left else "*"
    right_subtree = encode_tree_to_string(node.right) if node.right else "*"

    return f"{node.value}({left_subtree},{right_subtree})"


# Use the provided parsing and traversal functions
# ...

for i in range(20):
    # Generate a random tree and encode it to a string
    tree = generate_random_tree()
    tree_string = encode_tree_to_string(tree)

    # Parse the tree and compute traversals
    parsed_tree = parse_tree(tree_string)
    preorder = preorder_traversal(parsed_tree)
    inorder = inorder_traversal(parsed_tree)

    # Write input and output to files
    with open(f'data/{i}.in', 'w') as f_in:
        f_in.write(f"data/{tree_string}\n")

    with open(f'{i}.out', 'w') as f_out:
        f_out.write(f"{preorder}\n{inorder}\n")

    # Optionally, print to console for verification
    print(f"Input {i}: {tree_string}")
    print(f"Preorder: {preorder}")
    print(f"Inorder: {inorder}")
    print()

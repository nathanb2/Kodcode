from collections import deque

from data_structures.tree_node import TreeNode


class BinaryTree:

    def __init__(self):
        self.root = None

    def insert(self, root, data):
        # Base case: If the root is None, create a new TreeNode with the given data and return it
        if root is None:
            return TreeNode(data)

        # Recursive cases
        if data >= root.data:
            # If data is greater than or equal to root.data, insert data into the right subtree
            root.right = self.insert(root.right, data)
        else:
            # If data is less than root.data, insert data into the left subtree
            root.left = self.insert(root.left, data)

        # Return the root node
        return root

    def print_binary_tree(self, root):
        # If the tree is empty, print a message and return
        if not root:
            print("The binary tree is empty.")
            return

        # Use a queue for level-order traversal
        queue = deque([root])

        # Initialize a variable to keep track of the current level
        current_level = 0

        print(f"Level {current_level}: ", end="")

        while queue:
            # Number of nodes at the current level
            level_size = len(queue)

            # Iterate through all nodes at the current level
            for i in range(level_size):
                # Get the current node
                current_node = queue.popleft()

                # Print the current node's data
                print(current_node.data, end=" ")

                # Add the left child to the queue if it exists
                if current_node.left:
                    queue.append(current_node.left)

                # Add the right child to the queue if it exists
                if current_node.right:
                    queue.append(current_node.right)

                # If we're at the end of a level, move to the next line
                if i == level_size - 1:
                    print()
                    # Check if the queue is not empty to print the next level
                    if queue:
                        current_level += 1
                        print(f"Level {current_level}: ", end="")



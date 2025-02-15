import random

class BinaryTreeNode:
    def __init__(self, value):
        """
        Initialize a binary tree node with the given value.
        The node has left and right child nodes set to None initially.

        :param value: The value to store in the node.
        """
        self.val = value
        self.left = None
        self.right = None

    def __str__(self):
        """
        Return a string representation of the node's value.
        """
        return str(self.value)


class BinaryTree:
    def __init__(self):
        """
        Initialize an empty binary tree with a root node set to None.
        """
        self.root = None

    def insert(self, value):
        """
        Insert a value into the binary tree.

        :param value: The value to insert into the tree.
        """
        # TODO: Implement this method
        current = self.root
        new_node = BinaryTreeNode(value)
        pre = None

        if current is None:
            self.root = new_node
            return

        while current is not None:
            if value > current.val:
                pre = current
                current = current.right
            else:
                pre = current
                current = current.left

        if value > pre.val:
            pre.right = new_node
        else:
            pre.left = new_node

    def recursive_insert(self, value):
        curr = self.root
        pre = None
        if self.root is None:
            self.root = BinaryTreeNode(value)
            return

        def rec_helper(pre, curr):
            if curr is None:
                if value > pre.val:
                    pre.right = BinaryTreeNode(value)
                else:
                    pre.left = BinaryTreeNode(value)
            else:
                if value > curr.val:
                    rec_helper(curr, curr.right)
                else:
                    rec_helper(curr, curr.left)

        rec_helper(pre, curr)

    def find(self, value):
        """
        Find a node with the given value in the binary tree.

        :param value: The value to search for.
        :return: The node with the specified value, or None if not found.
        """
        # TODO: Implement this method
        current = self.root
        pre = None

        if current is None:
            return

        while current is not value:
            if value > current.val:
                pre = current
                current = current.right
            else:
                pre = current
                current = current.left

        return current.val

    def delete(self, value):
        """
        Delete a node with the specified value from the binary tree.

        :param value: The value of the node to delete.
        """
        # TODO: Implement this method
        pass

    def inorder_traversal(self, node):
        """
        Perform an in-order traversal of the tree starting from the given node.

        :param node: The starting node for in-order traversal.
        :return: A list of values representing the in-order traversal.
        """
        # TODO: Implement this method
        new_list = []
        if node is None:
            return []
        else:
            new_list.extend(self.inorder_traversal(node.left))
            new_list.append(node.val)
            new_list.extend(self.inorder_traversal(node.right))

        return new_list

    def preorder_traversal(self, node):
        """
        Perform a pre-order traversal of the tree starting from the given node.

        :param node: The starting node for pre-order traversal.
        :return: A list of values representing the pre-order traversal.
        """
        # TODO: Implement this method
        new_list = []
        if node is None:
            return []
        else:
            new_list.append(node.val)
            new_list.extend(self.preorder_traversal(node.left))
            new_list.extend(self.preorder_traversal(node.right))

        return new_list

    def postorder_traversal(self, node):
        """
        Perform a post-order traversal of the tree starting from the given node.

        :param node: The starting node for post-order traversal.
        :return: A list of values representing the post-order traversal.
        """
        # TODO: Implement this method
        new_list = []
        if node is None:
            return []
        else:
            new_list.extend(self.postorder_traversal(node.left))
            new_list.extend(self.postorder_traversal(node.right))
            new_list.append(node.val)
        return new_list

    def level_order_traversal(self):
        """
        Perform a level-order (breadth-first) traversal of the tree.

        :return: A list of values representing the level-order traversal.
        """
        # TODO: Implement this method
        cur = [self.root]
        temp = []
        full_list = []
        while (len(cur) != 0):
            for val in cur:
                full_list.append(val.val)
                if val.left is not None:
                    temp.append(val.left)
                if val.right is not None:
                    temp.append(val.right)
            cur = temp
            temp = []

        return full_list

    def is_empty(self):
        """
        Check if the binary tree is empty.
        return: True if the tree is empty, False otherwise.
        """
        if(self.root is None):
            return True
        return False


    def height(self, node):
        """
        Compute the height of the binary tree.

        :param node: The starting node to calculate the height from.
        :return: The height of the tree.
        """
        # TODO: Implement this method
        def height_helper(node):
            if node is None:
                return 0
            else:
                left = height_helper(node.left)
                right = height_helper(node.right)

            return max(left, right) + 1

        return height_helper(self.root)

    def min_value_node(self, node):
        """
        Find the node with the minimum value starting from the given node.

        :param node: The starting node to find the minimum value from.
        :return: The node with the minimum value.
        """
        # TODO: Implement this method

        while node.left is not None:
            node = node.left

        return node.val

    def max_value_node(self, node):
        """
        Find the node with the maximum value starting from the given node.

        :param node: The starting node to find the maximum value from.
        :return: The node with the maximum value.
        """
        # TODO: Implement this method

        while node.right is not None:
            node = node.right

        return node.val

tree = BinaryTree()
random.randint(0,100)
for i in range(10):
    tree.insert(random.randint(0,100))

print(tree.inorder_traversal(tree.root))
print(tree.preorder_traversal(tree.root))
print(tree.postorder_traversal(tree.root))
print(tree.level_order_traversal())
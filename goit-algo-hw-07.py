class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self, root):
        self.root = Node(root)

    def insert(self, value, node=None):
        if node is None:
            self.root = Node(value)
        else:
            if value < node.value:
                if node.left is None:
                    node.left = Node(value)
                else:
                    self.insert(value, node.left)
            else:
                if node.right is None:
                    node.right = Node(value)
                else:
                    self.insert(value, node.right)

    # task 1
    def find_max_value(self, node=None):
        if node is None:
            node = self.root
        if node.right is None:
            return node.value
        return self.find_max_value(node.right)

    # task 2
    def find_min_value(self, node=None):
        if node is None:
            node = self.root
        if node.left is None:
            return node.value
        return self.find_min_value(node.left)

    # task 3
    def find_sum_values(self, node=None):
        if node is None:
            node = self.root
        left_sum = self.find_sum_values(node.left) if node.left else 0
        right_sum = self.find_sum_values(node.right) if node.right else 0
        return node.value + left_sum + right_sum


bt = BinaryTree(10)
bt.insert(5, bt.root)
bt.insert(15, bt.root)
bt.insert(2, bt.root)
bt.insert(7, bt.root)
bt.insert(12, bt.root)
bt.insert(17, bt.root)

# Task 1
print(f'Max : {bt.find_max_value()}')

# Task 2
print(f'Min : {bt.find_min_value()}')

# Task 3
print(f'Sum : {bt.find_sum_values()}')

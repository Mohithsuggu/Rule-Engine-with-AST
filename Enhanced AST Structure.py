class Node:
    def __init__(self, node_type, left=None, right=None, value=None):
        self.type = node_type  # "operator" or "operand"
        self.left = left  # Reference to another Node (left child)
        self.right = right  # Reference to another Node (right child)
        self.value = value  # Value for operand nodes (e.g., number or string)

    def __repr__(self):
        if self.type == "operand":
            return f"Operand({self.value})"
        else:
            return f"Operator({self.value}, {self.left}, {self.right})"

import math


class Node:
    def __init__(self, value):
        self.value = value
        self.right = None
        self.left = None


# Function to validate BST
# Using semantics where left child is strictly less than parent
def validate_bst(root, low, high):
    if root is None:
        return True
    if root.value < low or root.value > high:
        return False

    return validate_bst(root.left, low, root.value - 1) and validate_bst(root.right, root.value + 1, high)


def main():
    root = Node(5)
    root.right = Node(6)
    root.right.right = Node(7)
    root.left = Node(3)
    root.left.right = Node(4)
    root.left.left = Node(0)

    '''
    root = Node(4)
    root.left = Node(2)
    root.right = Node(5)
    root.left.left = Node(1)
    root.left.right = Node(3)
    '''
    print(validate_bst(root, -math.inf, math.inf))


if __name__ == '__main__':
    main()
import math
import queue
import numpy

class Node:
    def __init__(self, value):
        self.value = value
        self.right = None
        self.left = None

# Helper function to perform level order tree traversal
# Saves all values in each level in a linked list
# Returns dict of LLs, keyed by level number
def ll_of_levels(root):
    q = queue.Queue()
    q.put((root, 0))

    ret = {}

    while not q.empty():
        curr, level = q.get()
        if curr is None:
            continue
        if level in ret:
            ret[level].append(curr.value)
        else:
            ret[level] = [curr.value]
        q.put((curr.left, level + 1))
        q.put((curr.right, level + 1))
    return ret

# Preorder traversal for debugging
def preorder(root):
    if root is None:
        return
    print(root.value)
    preorder(root.left)
    preorder(root.right)


# Function to create BST of minimal depth from sorted array
# Uses binary search variant to make a node have children with values
# in the middle of the two separated subarrays
def minimal_tree(arr, mindex, maxdex):
    if mindex > maxdex:
        return None
    else:
        mid = math.ceil((maxdex + mindex) / 2)
        node = Node(arr[mid])
        node.right = minimal_tree(arr, mid + 1, maxdex)
        node.left = minimal_tree(arr, mindex, mid - 1)

        return node

def main():
    arr = [0, 1, 2, 3, 4]
    n = minimal_tree(arr, 0, 4)
    print(ll_of_levels(n))

    arr = numpy.arange(0, 100, 1)
    n = minimal_tree(arr, 0, 99)
    print(ll_of_levels(n))

if __name__ == '__main__':
    main()
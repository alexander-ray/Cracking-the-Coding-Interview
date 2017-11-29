import queue


class Node:
    def __init__(self, value):
        self.value = value
        self.right = None
        self.left = None


# Function to perform level order tree traversal
# Prints nodes in a top-down, left-right order
def level_order_traversal(root):
    q = queue.Queue()
    q.put(root)

    while not q.empty():
        curr = q.get()
        if curr is None:
            continue
        print(curr.value)
        q.put(curr.left)
        q.put(curr.right)


# Function to perform level order tree traversal
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

def main():
    root = Node(5)
    root.right = Node(6)
    root.right.right = Node(7)
    root.left = Node(3)
    root.left.right = Node(4)
    root.left.left = Node(0)

    #level_order_traversal(root)
    print(ll_of_levels(root))

if __name__ == '__main__':
    main()
# Graph playground in python
# Includes implementations of DFS and BFS, as well as a Graph, Node, and other algorithms
# The search algorithms are acting as traversals, though the visit method can be altered to include a check

import queue

class Graph:
    def __init__(self, nodes):
        self.nodes = nodes

    def reset(self):
        for i in self.nodes:
            i.visited = False

class Node:
    def __init__(self, id):
        self.id = id
        self.neighbors = []
        self.visited = False

    def add_neighbor(self, node):
        self.neighbors.append(node)

# Visit method
# Can be extended to include a check for a given search
def visit_node(n):
    print("Node: " + str(n.id))

# Recursive version of DFS
def dfs_recursive(root):
    if (root == None):
        return
    visit_node(root)
    root.visited = True

    for i in root.neighbors:
        if (i.visited == False):
            dfs_recursive(i)

# Iterative version of DFS
# Uses stack as primary data structure
def dfs_iterative(root):
    q = queue.LifoQueue()

    # Visit root and add to queue
    root.visited = True
    q.put(root)

    while not q.empty():
        # Get node at front of queue, visit
        curr = q.get()
        visit_node(curr)
        # Iterate through neighbors, visiting as necessary
        # Add each neighbor to queue if not visited
        for i in curr.neighbors:
            if not i.visited:
                i.visited = True
                q.put(i)

# BFS
# Uses FIFO queue as primary data structure
def bfs(root):
    q = queue.Queue()

    # Visit root and add to queue
    root.visited = True
    q.put(root)

    while not q.empty():
        # Get node at front of queue, visit
        curr = q.get()
        visit_node(curr)
        # Iterate through neighbors, visiting as necessary
        # Add each neighbor to queue if not visited
        for i in curr.neighbors:
            if not i.visited:
                i.visited = True
                q.put(i)

def search_helper(graph):
    print("DFS Recursive:")
    dfs_recursive(graph.nodes[0])
    graph.reset()

    print("DFS Iterative:")
    dfs_iterative(graph.nodes[0])
    graph.reset()

    print("BFS:")
    bfs(graph.nodes[0])
    graph.reset()

def main():
   graph = Graph([Node(x) for x in range(0, 6)])
   g = graph.nodes
   g[0].add_neighbor(g[1])
   g[0].add_neighbor(g[4])
   g[0].add_neighbor(g[5])
   g[1].add_neighbor(g[3])
   g[1].add_neighbor(g[4])
   g[2].add_neighbor(g[1])
   g[3].add_neighbor(g[2])
   g[3].add_neighbor(g[4])

   search_helper(graph)

if __name__ == '__main__':
    main()
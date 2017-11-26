class Graph:
    def __init__(self, nodes):
        self.nodes = nodes

class Node:
    def __init__(self, id):
        self.id = id
        self.neighbors = []
        self.visited = False

    def add_neighbor(self, node):
        self.neighbors.append(node)

def dfs_recursive(root):
    if (root == None):
        return
    print("Node: " + str(root.id))
    root.visited = True

    for i in root.neighbors:
        if (i.visited == False):
            dfs_recursive(i)

def search_helper(graph):
    dfs_recursive(graph.nodes[0])

    # Reset graph
    for i in graph.nodes:
        i.visited = False

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
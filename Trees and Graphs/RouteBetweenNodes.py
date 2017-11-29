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

def path_exists(n1, target):
    n1.visited = True
    if n1.id == target.id:
        return True

    for e in n1.neighbors:
        if (not e.visited) and path_exists(e, target):
            return True

    return False
    
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
    print(path_exists(g[2], g[5]))

if __name__ == '__main__':
    main()

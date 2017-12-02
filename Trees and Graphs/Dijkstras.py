import math
import heapq

class Graph:
    def __init__(self, nodes):
        self.nodes = nodes

class Node:
    def __init__(self, id):
        self.id = id
        self.neighbors = []

    def add_neighbor(self, node, weight):
        self.neighbors.append((node, weight))


def dijkstras(g, start_id, target_id):
    remaining = []
    path_weight = [math.inf for _ in g]
    previous = [-1 for _ in g]

    path_weight[start_id] = 0
    heapq.heappush(remaining, (0, g[start_id].id, g[start_id]))

    while remaining:
        w, _, n = heapq.heappop(remaining)
        path_weight[n.id] = w
        previous[n.id] = n.id

        if n.id == target_id:
            return path_weight[n.id]

        for e, w2 in n.neighbors:
            if math.isinf(path_weight[e.id]):
                heapq.heappush(remaining, (path_weight[n.id] + w2, e.id ,e))
    return float("inf")

def main():
    graph = Graph([Node(x) for x in range(0, 6)])
    g = graph.nodes
    g[0].add_neighbor(g[1], 2)
    g[0].add_neighbor(g[4], 1)
    g[0].add_neighbor(g[5], 1)
    g[1].add_neighbor(g[3], 10)
    g[1].add_neighbor(g[4], 3)
    g[2].add_neighbor(g[1], 1)
    g[3].add_neighbor(g[2], 4)
    g[3].add_neighbor(g[4], 3)
    g[5].add_neighbor(g[3], 2)

    print(dijkstras(g, 0, 3))


if __name__ == '__main__':
    main()
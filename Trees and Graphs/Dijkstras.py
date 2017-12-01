import math
import queue

class Graph:
    def __init__(self, nodes):
        self.nodes = nodes

class Node:
    def __init__(self, id):
        self.id = id
        self.neighbors = []

    def add_neighbor(self, node, weight):
        self.neighbors.append((node, weight))


def dijkstras(g, target_id):
    print('hello')

def main():
    graph = Graph([Node(x) for x in range(0, 6)])
    g = graph.nodes
    g[0].add_neighbor(g[1], 2)
    g[0].add_neighbor(g[4], 1)
    g[0].add_neighbor(g[5], 1)
    g[1].add_neighbor(g[3], 5)
    g[1].add_neighbor(g[4], 3)
    g[2].add_neighbor(g[1], 1)
    g[3].add_neighbor(g[2], 4)
    g[3].add_neighbor(g[4], 3)



if __name__ == '__main__':
    main()
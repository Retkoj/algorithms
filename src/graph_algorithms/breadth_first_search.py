from src.graph_algorithms.graph import Graph, TraverseStates


class BreadthFirstSearch:
    def __init__(self, graph: Graph):
        self.graph = graph
        self.start_node = None
        self.predecessor = {}
        self.traversed = {}
        self.distances = {}
        self.queue = []
        self.graph_traversed = True

    def traverse_graph(self, start_node):
        self.start_node = start_node
        for node in self.graph.get_nodes():
            self.predecessor[node] = -1
            self.distances[node] = float("inf")
            self.traversed[node] = TraverseStates.NOT_VISITED

        self.traversed[start_node] = TraverseStates.VISITED
        self.distances[start_node] = 0

        self.queue = []
        self.queue.insert(0, start_node)

        while len(self.queue) > 0:
            current_node = self.queue.pop()
            for neighbor in self.graph.get_node_neighbors(current_node):
                if self.traversed[neighbor] == TraverseStates.NOT_VISITED:
                    self.predecessor[neighbor] = current_node
                    self.distances[neighbor] = self.distances[current_node] + 1
                    self.traversed[neighbor] = TraverseStates.VISITED

                    self.queue.insert(0, neighbor)

            self.traversed[current_node] = TraverseStates.ALL_NEIGHBOURS_VISITED
            self.graph_traversed = True

    def find_path_to_node(self, target_node, start_node=None):
        """
        Given a target node, find the path from the start node to that target node.
        Works by recursively looking up the predecessor nodes, starting at the target node and stopping when
        the start node is reached. The returned list contains the starting node and the nodes that need to be
        passed to get to the target node.

        :param target_node: str, The end node
        :param start_node: str, Root node, defaults to self.start_node
        :return: list, [start_node, node_1, node_2, ..., node_n, target_node]
        """
        if self.graph_traversed:
            start_found = False
            start_node = start_node if start_node else self.start_node
            path = []
            current_node = target_node
            while not start_found:
                path.append(current_node)
                current_node = self.predecessor[current_node]
                if current_node == start_node:
                    start_found = True
                    path.append(current_node)
            path.reverse()
            return path
        else:
            print("Graph not traversed yet. Call the traverse_graph function first.")
            return None


if __name__ == '__main__':
    graph = Graph(['A', 'B', 'C', 'D', 'E'], directed=False)
    graph.add_edge('A', 'B')
    graph.add_edge('B', 'C')
    graph.add_edge('C', 'D')
    graph.add_edge('D', 'E')
    graph.add_edge('B', 'E')
    depth_first_search = BreadthFirstSearch(graph)
    depth_first_search.traverse_graph(start_node='A')

    assert depth_first_search.find_path_to_node('E') == ['A', 'B', 'E']
    assert depth_first_search.find_path_to_node('D') == ['A', 'B', 'C', 'D']
    assert depth_first_search.find_path_to_node('E', start_node='B') == ['B', 'E']

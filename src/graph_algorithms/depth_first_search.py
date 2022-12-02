from enum import Enum

from src.graph_algorithms.graph import Graph


class TraverseStates(Enum):
    VISITED = 'grey'
    ALL_NEIGHBOURS_VISITED = 'black'
    NOT_VISITED = 'white'


class DepthFirstSearch:
    def __init__(self, graph: Graph):
        self.graph = graph
        self.traversed = {}
        self.predecessor = {}
        self.start_node = None
        self.graph_traversed = False

    def _visit_node(self, node):
        self.traversed[node] = TraverseStates.VISITED
        for neighbor in self.graph.get_node_neighbors(node):
            if self.traversed[neighbor] == TraverseStates.NOT_VISITED:
                self.predecessor[neighbor] = node
                self._visit_node(neighbor)
            self.traversed[node] = TraverseStates.ALL_NEIGHBOURS_VISITED

    def traverse_graph(self, start_node):
        self.start_node = start_node
        for node in self.graph.get_nodes():
            self.predecessor[node] = -1
            self.traversed[node] = TraverseStates.NOT_VISITED
        self._visit_node(start_node)
        self.graph_traversed = True

    def find_path_to_node(self, target_node, start_node=None):
        if self.traversed:
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
    graph.add_edge('B', 'E')
    depth_first_search = DepthFirstSearch(graph)
    depth_first_search.traverse_graph(start_node='A')

    assert depth_first_search.find_path_to_node('E') == ['A', 'B', 'E']
    assert depth_first_search.find_path_to_node('D') == ['A', 'B', 'C', 'D']
    assert depth_first_search.find_path_to_node('D', start_node='B') == ['B', 'C', 'D']

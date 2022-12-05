from enum import Enum

from src.graph_algorithms.graph import Graph


class TraverseStates(Enum):
    """Helper class for node states during graph traversal"""
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
        """
        Recursive function to visit the node and its neighbors. When a neighbor is found, this function is called
        with that node.
        Adds the neighbor to self.predecessor and sets its value to node.

        :param node: str, current node
        """
        self.traversed[node] = TraverseStates.VISITED
        for neighbor in self.graph.get_node_neighbors(node):
            if self.traversed[neighbor] == TraverseStates.NOT_VISITED:
                self.predecessor[neighbor] = node
                self._visit_node(neighbor)
            self.traversed[node] = TraverseStates.ALL_NEIGHBOURS_VISITED

    def traverse_graph(self, start_node):
        """
        Walks the graph starting at start_node. Self.start_node is set, to have a default for the path finding
        function. (Another possibility to find start node(s) would be to find the key(s) where
        self.predecessor[node] == -1)
        Starts by setting all nodes in the graph to 'not visited', then the recursive '_visit_node' function is called
        to traverse all nodes and neighbors.
        Finally, self.graph_traversed is set to true, to indicate self.graph is processed

        :param start_node: str, root node from where to walk the graph
        """
        self.start_node = start_node
        for node in self.graph.get_nodes():
            self.predecessor[node] = -1
            self.traversed[node] = TraverseStates.NOT_VISITED

        self._visit_node(start_node)
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

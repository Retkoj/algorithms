class Graph:
    def __init__(self, nodes: int or list, directed=False):
        """

        :param nodes: int or list, if int, node labels are set to the range [0 - nodes],
            If nodes is a list, the node labels are set to that list (items cast to strings)
        :param directed: bool, whether it's a directed (True) or undirected (False) graph, defaults to undirected
        """
        self.nodes = nodes
        self.node_labels = []
        self.directed = directed
        self.graph = {}
        self._create_graph()

    def _create_graph(self):
        """
        Create a graph dict with node labels as keys.
        If self.nodes is an int, the node labels are in the range 0 - self.nodes.
        If self.nodes is a list, the node labels are set to that list (items cast to strings)
        """
        if type(self.nodes) == int:
            self.node_labels = list(range(0, self.nodes))
        elif type(self.nodes) == list:
            self.node_labels = [str(node) for node in self.nodes]

        self.graph = {node: {} for node in self.node_labels}

    def get_nodes(self) -> list:
        """Returns all nodes in the graph"""
        return self.node_labels

    def get_node_neighbors(self, node) -> set:
        """Get all neighbor node labels of node"""
        return self.graph[node].keys()

    def add_edge(self, node, target_node, weight=0):
        """
        Adds the edge (node, target_node) with a weight.
        If the graph is undirected, also adds the edge (target_node, node).

        :param node: str, source node of edge
        :param target_node: str, target node of edge
        :param weight: int, weight of the edge, default 0
        """
        if target_node not in self.graph[node].keys():
            self.graph[node][target_node] = weight
        if not self.directed:
            if node not in self.graph[target_node].keys():
                self.graph[target_node][node] = weight

    def remove_edge(self, node, target_node):
        """
        Removes the edge (node, target_node).
        If the graph is undirected, also removes the edge (target_node, node).

        :param node: str, source node of edge
        :param target_node: str, target node of edge
        """
        if target_node not in self.graph[node].keys():
            del self.graph[node][target_node]
        if not self.directed:
            if node not in self.graph[target_node].keys():
                del self.graph[target_node][node]

    def edge_exists(self, node, target_node):
        """Check if the edge (node, target_node) exists in self.graph"""
        return target_node in self.graph[node].keys()

    def get_edge_weight(self, node, target_node):
        """If edge (node, target_node) exists, returns weight of the edge, otherwise returns None"""
        if target_node in self.graph[node].keys():
            return self.graph[node][target_node]
        else:
            return None

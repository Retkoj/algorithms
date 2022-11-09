from enum import Enum

from treelib import Tree


class Player(Enum):
    MAX = 1
    MIN = -1


class MinMaxTreeGame:
    """
    Game where every node branches into 2 children nodes, with end nodes containing values.
    Goal of a MAX player would be to get the highest end node value, the min player wants the lowest possible
    end node. In every round, the player must choose one of the 2 valid nodes.

    The following tree is used:

    root
    ├── l1
    │   ├── l1-1: 3
    │   └── l1-2: 5
    └── r1
        ├── r1-1: 2
        └── r1-2: 9
    """
    def __init__(self):
        self.tree = Tree()
        self.create_simple_tree()
        self.current_node_id = self.tree.root

    def create_simple_tree(self):
        """A hardcoded tree"""
        self.tree.create_node(data=None, tag="root", identifier="root")
        self.tree.create_node(data=None, tag="l1", identifier="l1", parent='root')
        self.tree.create_node(data=None, tag="r1", identifier="r1", parent='root')
        self.tree.create_node(data=3, tag="l1-1: 3", identifier="l1-1", parent='l1')
        self.tree.create_node(data=5, tag="l1-2: 5", identifier="l1-2", parent='l1')
        self.tree.create_node(data=2, tag="r1-1: 2", identifier="r1-1", parent='r1')
        self.tree.create_node(data=9, tag="r1-2: 9", identifier="r1-2", parent='r1')

    def make_move(self, node_id):
        """Make a move to the node at node_id"""
        self.current_node_id = node_id

    def undo_move(self, node_id):
        """Undo the move to node_id by moving back to the parent node, if the current node isn't a root node"""
        if self.tree.level(node_id) > 0:
            self.current_node_id = self.tree.parent(node_id).identifier
        else:
            self.current_node_id = node_id

    def evaluate(self):
        """In this case, evaluating the game simply means returning te current node's data value"""
        return self.tree.get_node(self.current_node_id).data

    def get_valid_moves(self):
        """Valid moves are all children node id's of the current node"""
        return [node.identifier for node in self.tree.children(self.current_node_id)]

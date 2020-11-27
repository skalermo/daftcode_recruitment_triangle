MAX_VAL = 1_000_000
MIN_VAL = 1


class PathTree:
    def __init__(self):
        self.root = None
        self.leaves = []
        self.height = 0

    def add_leaves(self, nodes):
        assert len(self.leaves) + 1 == len(nodes)
        if not self.leaves:
            self.root = nodes[0]
            self.root.cum_value = self.root.value

        for i in range(len(self.leaves)):
            self.leaves[i].left = nodes[i]
            self.leaves[i].right = nodes[i+1]

        self.leaves = nodes
        self.height += 1
        for leaf in self.leaves:
            leaf.height = self.height

    def find_best_path(self):
        opened_nodes = set()
        closed_nodes = set()
        opened_nodes.add(self.root)
        current_node = self.root

        while current_node.height != self.height:
            next_nodes = current_node.get_children()

            for node in next_nodes:
                if node not in closed_nodes:
                    opened_nodes.add(node)
            opened_nodes.remove(current_node)

            current_node = min(opened_nodes,
                               key=lambda node: node.cum_value + self._heuristic_value(node))
            closed_nodes.add(current_node)
        current_node.backtrack_and_set_path()

        best_path = []
        node = self.root
        while node:
            best_path.append(node)
            node = node.next_node
        return best_path, best_path[-1].cum_value

    def _heuristic_value(self, node):
        return (self.height - node.height) * MIN_VAL


class Node:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.parent = None
        self.height = None
        self.cum_value = MAX_VAL
        self.value = value
        self.next_node = None

    def __repr__(self):
        return str(self.value)

    def get_children(self):
        if self.left.cum_value > self.left.value + self.cum_value:
            self.left.cum_value = self.left.value + self.cum_value
            self.left.parent = self
        if self.right.cum_value > self.right.value + self.cum_value:
            self.right.cum_value = self.right.value + self.cum_value
            self.right.parent = self
        return self.left, self.right

    def backtrack_and_set_path(self):
        if self.parent:
            self.parent.next_node = self
            self.parent.backtrack_and_set_path()

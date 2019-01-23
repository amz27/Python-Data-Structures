#!/usr/bin/python

class GraphNode():
    """Class-Based Node in Graph."""

    def __init__(self, key):
        """Initialize the GraphNode Object."""
        self.key = key
        self.outEdges = dict()
        self.inEdges = dict()

    def add_edge(self, other, edge_value=1):
        """Add edge to the node with the associated edge value (1 by default)."""
        self.outEdges[other] = edge_value
        other.inEdges[self] = edge_value

    def remove_outward_edge(self, other, complete=True):
        """Remove outgoing edge from this node (remove inward edge from other if complete=True)."""
        if other in self.outEdges.keys():
            del self.outEdges[other]
            if complete:
                other.remove_inward_edge(self, False)

    def remove_inward_edge(self, other, complete=True):
        """Remove incoming edge from this node (remove outward edge from other if complete=True)."""
        if other in self.inEdges.keys():
            del self.inEdges[other]
            if complete:
                other.remove_outward_edge(self, False)

    def remove_from_graph(self, maintain_connections=False):
        """Remove Node from graph, maintaining memory of connections."""
        for i in self.outEdges.keys():
            i.remove_inward_edge(self, False)

        for i in self.inEdges.keys():
            i.remove_outward_edge(self, False)

        if not maintain_connections:
            self.outEdges.clear()
            self.inEdges.clear()

    def __del__(self):
        """Overwrite standard implementation to remove edges."""
        self.remove_from_graph()

    def __str__(self):
        """Provide String representation of GraphNode."""
        return "<" + str(self.key) + ":" + str(self.outEdges) + ">"

    def __repr__(self):
        """Provide in-context representation of GraphNode."""
        return str(self.key)


class Graph():
    """Class-based representation of a generalized graph."""

    def __init__(self, undirected=True):
        """Initialize Graph variables."""
        self.nodes = dict()  # Hashes the key of each node to its GraphNode
        self.undirected = undirected  # Flag for directed/ undirected graph

    def create_node(self, key):
        """Overwrite this class to use a different node implementation."""
        return GraphNode(key)

    def add_or_get_node(self, key):
        """Add node to the graph if it does not exist. Return node if it does."""
        if key not in self.nodes.keys():
            newNode = self.create_node(key)
            self.nodes[key] = newNode
        return self.nodes[key]

    def add_node(self, key):
        """Add node to the graph if it does not exist."""
        self.add_or_get_node(key)

    def add_edge(self, head_key, tail_key, edge_value=1):
        """Add edge from the node corresponding to head_key to the one corresponding to tail_key."""
        if head_key == tail_key:
            return

        node_head = self.add_or_get_node(head_key)
        node_tail = self.add_or_get_node(tail_key)

        node_head.add_edge(node_tail, edge_value)
        if self.undirected:
            node_tail.add_edge(node_head, edge_value)

    def remove_edge(self, head_key, tail_key):
        """Remove edge from the node corresponding to head_key to the one corresponding to tail_key."""
        node_head = self.add_or_get_node(head_key)
        node_tail = self.add_or_get_node(tail_key)

        node_head.remove_outward_edge(node_tail)
        if self.undirected:
            node_tail.remove_inward_edge(node_head)

    def remove_node(self, node_key):
        """Remove node corresponding to node_key from the graph."""
        node = self.add_or_get_node(node_key)
        node.remove_from_graph(True)
        del self.nodes[node_key]
        return node

    def delete_node(self, node_key):
        """Delete node corresponding to node_key from the graph."""
        node = self.remove_node(node_key)
        del node

    def get_outedges(self, node_key):
        """Get keys corresponding to the outedges of a given node_key."""
        if node_key not in self.nodes.keys():
            return []
        arr = [a.key for a in self.add_or_get_node(node_key).outEdges.keys()]
        return arr

    def get_inedges(self, node_key):
        """Get keys corresponding to the inedges of a given node_key."""
        if node_key not in self.nodes.keys():
            return []
        arr = [a.key for a in self.add_or_get_node(node_key).inEdges.keys()]
        return arr

    def __str__(self):
        """Provide a basic string representation of the graph."""
        return str(dict)

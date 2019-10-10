from anytree import NodeMixin, PostOrderIter
from graphviz import Digraph

class Node(NodeMixin):
    def __init__(self, name, parent=None, weight=0):
        self.name = name
        self.parent = parent
        self.weight = weight


        ############
class ParcialTree:
    def __init__(self, node):
        self.node = node
        self.graph = Digraph()
        self.init()

    def init(self):
        node = self.node
        while node.parent:
            for child in node.parent.children:
                self.graph.node(str(id(child)), child.name, color='lightblue2', style='filled')
            node = node.parent
        self.graph.node(str(id(node)), node.name, color='lightblue2', style='filled')

        node = self.node
        self.graph.node(str(id(node)), node.name, color='red')
        while node.parent:
            self.graph.node(str(id(node.parent)), node.parent.name, color='red')
            node = node.parent

        node = self.node
        while node.parent:
            for child in node.parent.children:
                self.graph.edge(str(id(node.parent)), str(id(child)))
            node = node.parent

    def render(self):
        self.graph.render(format='png')


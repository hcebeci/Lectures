
# not object oriented!!
class Node:
    def __init__(self, code: str,successor_nodes = [],predecessor_nodes = []) -> None:
        self.successor_nodes = successor_nodes
        self.predecessor_nodes = predecessor_nodes
        self.code = code
class DAG:
    def __init__(self) -> None:
         self.nodes = []
         self.arcs = []

         self.nodes.append(Node(1))
         self.nodes.append(Node(2))         
         self.nodes.append(Node(3))

         self.arcs.append(Arc(self.nodes[0], self.nodes[1], 3))
         self.arcs.append(Arc(self.nodes[0], self.nodes[2], 10))
         self.arcs.append(Arc(self.nodes[1], self.nodes[2], 5))

    def initialize_pred_succ_nodes(self):   #nodedaki listeleri dolduracak function
        for node in self.nodes:
            for arc in self.arcs:
                if node == arc.from_node:
                    num = arc.to_node.code
                    node.successor_nodes.append(Node(num))#.append(Node(num))
                    print('node', node.code, ' dan sonra gelen node', num)
                if node == arc.to_node:
                    num = arc.from_node.code
                    node.predecessor_nodes.append(Node(num))
                    print('node', node.code, ' dan once gelen node', num)

    def incomming_arcs(self, v: Node):
        # Discuss performance

        inarcs = []
        for a in self.arcs:
            if (a.to_node == v):
                inarcs.append(a)
        return inarcs

    def SP(self, s : Node, v: Node) -> int:
        # Discuss performance

        min = 0
        for a in self.incomming_arcs(v):
            length = a.distance + self.SP(s, a.from_node)
            if (min <= 0 or length < min):
                min = length

        return min
class Arc:
    def __init__(self, from_node: Node, to_node: Node, distance: int) -> None:
        self.from_node = from_node
        self.to_node = to_node
        self.distance = distance

d = DAG()
#for a in d.arcs:
#   print(a.from_node.successor_nodes)
d.initialize_pred_succ_nodes()
print(Node(1).successor_nodes.code,Node(1).predecessor_nodes.code)

# Really. Not object oriented!!
#print (d.SP(d.nodes[0], d.nodes[2]))







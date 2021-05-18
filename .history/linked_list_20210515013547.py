class Node:
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next_node = next_node


node2 = Node()
node1 = Node("data", node2)


class Linked_list:
    def __init__(self):
        self.head = None
        self.last_node = None


def print_ll(self):
    ll_string = ""
    node = self.head
    if node is None:
        print(None)
    while node:
        ll_string += f"{str(node.data)} ->"
        node = node.next_node
    ll_string += "None"
    print(ll_string)


ll = Linked_list()
node4 = Node("data", None)
node3 = Node("data", node4)
node2 = Node("data", node3)
node1 = Node("data", node2)

ll.head = node1

ll.print_ll()

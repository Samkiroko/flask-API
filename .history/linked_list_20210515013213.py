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
    if node is Non:
        print(None)
    while node:
        ll_string += f"{str(node.data)} ->"
        node = node.next_node
    ll_string += "None"
    print(ll_string)

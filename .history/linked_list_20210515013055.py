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
        if node.next_node is None:
            ll_string += "None"
        node = node.next_node
    print(ll_string)

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

node1 = Node(12)
node2 = Node(99)
node4 = Node(37)

node1.next = node2 # 12 - 99
node2.next = node3 # 99 -37

## the entire linked list -> 12 - 99 - 77

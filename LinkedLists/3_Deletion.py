class Node:
    def __init__(self,data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

## front side
    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

## insert any place
    def InsertAfter(self, prev_node, new_data):
        new_node = Node(new_data)
        new_node.next = prev_node.next
        prev_node.next = new_node

## back side
    def append(self, new_data):
        new_node = Node(new_data)

        if self.head is None:
            self.head = new_node
            return

        last = self.head
        while last.next:
            last = last.next

        last.next = new_node

## delete Node
    def deleteNode(self,key):
        temp = self.head

        if temp != None:
            if temp.data == key:
                self.head = temp.next
                temp = None
                return

        while temp != None:
            if temp.data == key:
                break
            prev = temp
            temp = temp.next

        if temp == None:
            return

        prev.next = temp.next
        temp = None


    def printList(self):
        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.next

## start
if __name__ == "__main__":
    llist = LinkedList()
    llist.push(7)
    llist.push(1)
    llist.push(3)
    llist.push(2)
    print("Before Deletion")
    llist.printList()
    llist.deleteNode(1)
    print("After Deletion")
    llist.printList()

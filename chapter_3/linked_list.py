class Node():

    def __init__(self, data):
        self.next = None
        self.data = data

    def append_to_tail(self, data):
        end = Node(data)
        n = self
        while n.next is not None:
            n = n.next
        n.next = end


class LinkedList():

    def __init__(self, data):
        self.head = Node(data)

    def delete_node(self, data):
        n = self.head
        
        if n.data == data:
            self.head = n.next
        
        while n.next is not None:
            if n.next.data == data:
                n.next = n.next.next
                return n.next
            n = n.next

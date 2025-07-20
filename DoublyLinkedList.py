class Node:
    def __init__(self, val):
        self.val = val
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def is_empty(self):
        return self.head is None

    def append(self, data):
        new_node = Node(data)
        if self.is_empty():
            self.head = new_node
            self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node

    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head.prev = new_node
        self.head = new_node

    def delete(self, data):
        current = self.head
        while current:
            if current.val == data:
                if current.prev:
                    current.prev.next = current.next
                else:
                    self.head = current.next

                if current.next:
                    current.next.prev = current.prev
                else:
                    self.tail = current.prev
            current = current.next
        

    def display_reverse(self):
        current = self.tail
        data = []
        while current:
            data.append(current.val)
            current = current.prev
        print(data)

    def display(self):
        current = self.head
        data = []
        while current:
            data.append(current.val)
            current = current.next
        print(data)
        

    def __iter__(self):
        current = self.head
        while current:
            yield current.val
            current = current.next

if __name__ == '__main__':
    l = DoublyLinkedList()
    print(l.is_empty())
    l.append(5)
    l.prepend('data')
    l.prepend('Check')
    l.prepend('data')
    l.delete('data')
    print([item for item in l])
    l.display_reverse()
    l.display()

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def is_empty(self):
        return self.head is None

    def remove_first_node(self):
        if self.is_empty():
            return None

        data = self.head.data
        self.head = self.head.next
        if not self.head:
            self.tail = None
        return data

    def remove_last_node(self):
        if self.is_empty():
            return
        elif self.head.next is None:
            self.head = None
            self.tail = None
            return
        current = self.head
        while current and current.next:
            if current.next.next is None:
                current.next = None
                self.tail = current
                return
            current = current.next

    def append(self, data):
        new_node = Node(data)
        if self.head == None:
            self.head = new_node
            self.tail = self.head
        else:
            self.tail.next = new_node
            self.tail = new_node

    def prepend(self, data):
        new_node = Node(data)
        if self.is_empty():
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node


    def delete(self, data):
        if self.is_empty():
            return
        
        current = self.head
        if current and current.data == data:
            self.remove_first_node()
            return
        
        while current.next and current.next.data != data:
            current = current.next

        if current.next:
            if current.next == self.tail:
                self.tail = current
            current.next = current.next.next
        else:
            print('There is no node in the list with the given data')

    def insert_at_index(self, data, index):
        position = 0
        current = self.head
        while current is not None and position != index:
            position += 1
            current = current.next

        if current is not None:
            new_node = Node(data)
            new_node.next = current.next
            current.next = new_node
            if new_node.next is None:
                self.tail = new_node
        else:
            print('Index is not in the range of list')

    def size(self):
        if self.is_empty():
            count = 0
        count = 1
        current = self.head
        while current.next:
            count =+ 1
        return count
            
    def __iter__(self):
        current = self.head
        while current:
            yield current.data
            current = current.next
            

    def display(self):
        elements = []
        current = self.head
        while current:
            elements.append(str(current.data))
            current = current.next
        print('->'.join(elements))
            
if __name__ == "__main__":
    l = LinkedList()
    l.append(10)
    l.append(20)
    l.append(20)
    print(l.remove_first_node(), 'first_node')
    l.prepend("data")
    l.display()
    l.insert_at_index(3, 2)
    l.insert_at_index(3, 4)
    l.delete("data")
    l.delete(3)
    l.delete(10)
    l.display()

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def remove_first_node(self):
        if self.head is None:
            return

        self.head = self.head.next

    def append(self, data):
        if self.head == None:
            self.head = Node(data)
        else:
            last_node = self.head
            while last_node.next != None:
                last_node = last_node.next
            last_node.next = Node(data)

    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def delete(self, data):
        current = self.head

        if current is not None and current.data == data:
            self.remove_first_node()
            return
        while current is not None and current.next is not None:
            if current.next.data == data:
                current.next = current.next.next
                return
            current = current.next

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
        else:
            print('Index is not in the range of list')
                

    def display(self):
        current = self.head
        while current.next != None:
            print(f'{current.data} ->', end=" ")
            current = current.next
        print(f'{current.data}')
            

l = LinkedList()
l.append(10)
l.append(20)
l.prepend("data")
l.insert_at_index(3, 2)
l.insert_at_index(3, 4)
l.delete("data")
l.delete(3)
l.delete(10)
l.display()

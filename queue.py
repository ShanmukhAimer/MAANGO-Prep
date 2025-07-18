from linked_list import Node, LinkedList

class Queue:
    def __init__(self):
        self.bag = LinkedList()

    def enqueue(self, item):
        self.bag.append(item)

    def dequeue(self):
        data = self.bag.remove_first_node()
        return data

    def peek(self):
        head = self.bag.head
        return head.data if head else None

    def is_empty(self):
        return self.bag.is_empty()

    def size(self):
        return self.bag.size()

    def __repr__(self):
        elements = [item for item in self.bag]
        return f'Here is the final queue: {elements}'

l = Queue()
l.enqueue(10)
l.enqueue(20)
dequeued = l.dequeue()
peek = l.peek()
is_empty = l.is_empty()
size = l.size()
print(f'Dequeued value {dequeued}')
print(size, is_empty, peek)
print(l)

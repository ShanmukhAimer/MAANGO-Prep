class List:
    def __init__(self):
        self.l = []

    def push(self, data):
        self.l.append(data)

    def pop(self):
        if not self.is_empty():
            self.l.pop()
        return None

    def is_empty(self):
        return self.l

    def peek(self):
        if not self.is_empty():
            return self.l[self.size()-1]
        return None

    def size(self):
        return len(self.l)

    def __repr__(self):
        return f"Here is the final list: {self.l}"


l = List()
l.push(2)
l.pop()
l.push(3)
l.is_empty()
l.size()
l.peek()
print(l)

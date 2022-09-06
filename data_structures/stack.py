class Stack:
    def __init__(self):
        self.items = []
    def isEmpty(self):
        return self.items == []
    def pop(self):
        try:
            return self.items.pop()
        except IndexError as e:
            return "Sorry out of item", e
    def push(self, item):
        self.items.append(item)
    def peek(self):
        return self.items[len(self.items)-1]
    def size(self):
        return len(self.items)

stack = Stack()
stack.push("Red")
stack.push("Green")
stack.push("Blue")
stack.push("Yellow")
stack.size()
stack.pop()
stack.size()
stack.peek()
stack.isEmpty()
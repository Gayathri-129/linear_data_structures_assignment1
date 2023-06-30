
class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()

    def reverse(self):
        if not self.is_empty():
            item = self.pop()
            self.reverse()
            self.insert_at_bottom(item)

    def insert_at_bottom(self, item):
        if self.is_empty():
            self.push(item)
        else:
            top_item = self.pop()
            self.insert_at_bottom(item)
            self.push(top_item)

    def print_stack(self):
        print("Reversed Stack:")
        for item in self.items[::-1]:
            print(item)

stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
stack.push(4)
stack.push(5)

print("Original Stack:")
stack.print_stack()

stack.reverse()

stack.print_stack()

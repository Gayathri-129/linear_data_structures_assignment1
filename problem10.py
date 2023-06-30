class Stack:
    def __init__(self):
        self.items = []
        self.minimum_stack = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

        if self.minimum_stack:
            current_min = self.minimum_stack[-1]
            if item < current_min:
                self.minimum_stack.append(item)
            else:
                self.minimum_stack.append(current_min)
        else:
            self.minimum_stack.append(item)

    def pop(self):
        if not self.is_empty():
            self.minimum_stack.pop()
            return self.items.pop()

    def get_minimum(self):
        if not self.is_empty():
            return self.minimum_stack[-1]

    def print_stack(self):
        print("Stack:")
        for item in self.items[::-1]:
            print(item)


stack = Stack()
stack.push(5)
stack.push(3)
stack.push(7)
stack.push(2)
stack.push(8)

stack.print_stack()

minimum = stack.get_minimum()
print("Smallest number:", minimum)
from data_structures.linked_stack import LinkedStack


class SizedLinkedStack(LinkedStack):


    def __init__(self, capacity: int):
        super().__init__()
        self.capacity = capacity
        self.size = 0


    def push(self, data: any):
        if self.size >= self.capacity:
            return "error"

        self.size += 1
        super().push(data)

    def pop(self):

        if self.size >= 0:
            self.size -= 1

        return super().pop()
from typing import Type

from node import Node


class LinkedList:

    def __init__(self):
        self.head = None

    def append(self, data) -> Node:
        new_node = Node(data)

        if self.head == None:
            self.head = new_node
        else:
            current_node = self.head
            while current_node != None:
                if current_node.next == None:
                    current_node.next = new_node
                    break
                current_node = current_node.next

        return new_node

    def pop(self) -> Node:
        to_return = None
        if self.head == None:
            return None
        elif self.head.next == None:
            to_return = self.head
            self.head = None
        else:
            current_node = self.head
            while current_node.next:
                if not current_node.next.next:
                    to_return = current_node.next
                    current_node.next = None
                current_node = current_node.next
        return to_return

    def push(self, data) -> Node:
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def remove(self, data):
        if self.head == None:
            return
        elif self.head.next == None:
            if self.head.data == data:
                self.head = None
            else:
                return
        previous = self.head
        current = self.head.next
        while current:
            if current.data == data:
                previous.next = current.next
                current = None
            previous = current
            current = current.next

    def reverse(self) -> Type['LinkedList']:
        prev = None
        current = self.head
        while current:
            next_node = current.next
            current.next = prev
            if next_node:
                prev = current
                current = next_node
            else:
                self.head = current
        return self

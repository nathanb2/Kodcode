from typing import Type

from linkedlist.node import Node


class LinkedList:

    def __init__(self):
        self.head = None


    def push(self, data) -> Node:
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def pop_head(self) -> Node:

        if(not self.head):
            return None

        head = self.head
        self.head = self.head.next
        return head

    def peek_head(self) -> Node:
        return self.head

    def append(self, data: any) -> Node:

        # create new node with inputed data
        new_node = Node(data)

        # if linkedList is empty new_node will be the head
        if not self.head:
            self.head = new_node
            return new_node

        current_node = self.head

        while current_node:

            if not current_node.next:
                current_node.next = new_node
                return new_node
            else:
                current_node = current_node.next


    def pop(self) -> Node:

        if not self.head:
            return None
        elif not self.head.next:
            current_node = self.head
            self.head = None
            return current_node

        previous_node = self.head
        current_node = self.head.next

        while current_node:

            if not current_node.next:
                previous_node.next = None
                return current_node
            else:
                previous_node = current_node
                current_node = current_node.next


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

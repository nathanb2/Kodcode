from linkedlist.linkedlist import LinkedList
from linkedlist.node import Node


class LinkedStack:

    def __init__(self):
        self.__linked_list = LinkedList()

    def push(self, data: any):
        self.__linked_list.push(data)

    def pop(self) -> any:
        head: Node = self.__linked_list.pop_head()

        if not head:
            return None

        return head.data

    def peek(self) -> any:

        head: Node = self.__linked_list.peek_head()

        if not head:
            return None

        return head.data


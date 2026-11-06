from node import Node


class LinkedStack:
    """Stack implementation using a singly linked list."""

    def __init__(self):
        self.top = None

    def is_empty(self):
        return self.top is None

    def push(self, value):
        node = Node(value)
        node.next = self.top
        self.top = node

    def pop(self):
        if self.is_empty():
            raise IndexError("Stack underflow: cannot pop from an empty stack.")
        value = self.top.value
        self.top = self.top.next
        return value

    def peek(self):
        if self.is_empty():
            raise IndexError("Stack is empty: no top element to view.")
        return self.top.value

    def __str__(self):
        values = []
        current = self.top
        while current is not None:
            values.append(str(current.value))
            current = current.next
        return "Top -> " + (" -> ".join(values) if values else "None")

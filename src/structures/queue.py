from __future__ import annotations
from typing import Any, Optional
from dataclasses import dataclass


@dataclass
class QueueNode:
    value: Any
    next: Optional[QueueNode] = None


class Queue:
    def __init__(self, value=None):
        if value is None:
            self.head = None
            self.len = 0
        else:
            node = QueueNode(value)
            self.head = node
            self.len = 1
        self.tail = self.head

    def push(self, value):
        if self.len <= 0:
            node = QueueNode(value)
            self.head = node
            self.tail = node
        else:
            node = QueueNode(value)
            node.next = QueueNode(self.tail)
            self.tail.next = node
            self.tail = node

        self.len += 1

    def front(self):
        if self.len <= 0:
            raise IndexError("queue is empty")
        return self.head.value

    def pop(self):
        if self.len <= 0:
            raise ValueError("cannot pop from empty queue")
        value = self.head.value

        self.head = self.head.next

        self.len -= 1
        return value

    def size(self):
        return self.len

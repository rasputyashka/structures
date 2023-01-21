from __future__ import annotations
from dataclasses import dataclass
from typing import Any, Optional


@dataclass
class StackNode:
    value: Any
    prev: Optional[StackNode] = None


class Stack:
    def __init__(self, value=None):
        if value is None:
            self.head = None
            self.len = 0
        else:
            self.head = StackNode(value)
            self.len = 1

    def push(self, value):
        node = StackNode(value, self.head)
        self.head = node
        self.len += 1

    def top(self):
        if self.len <= 0:
            raise IndexError("Empty stack")
        return self.head.value

    def pop(self):
        if self.len <= 0:
            raise ValueError("Can not pop from empty stack")
        value = self.head.value
        self.head = self.head.prev
        self.len -= 1
        return value

    def size(self):
        return self.len

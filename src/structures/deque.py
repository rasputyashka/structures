"""This module is untested, probably it contains bugs"""


from __future__ import annotations
from typing import Any, Optional
from dataclasses import dataclass


@dataclass
class DequeNode:
    value: Any
    nxt: Optional[DequeNode] = None
    prev: Optional[DequeNode] = None


# H N N T
# T P P H


class Deque:
    def __init__(self, value=None):
        if value is None:
            self.head = None
            self.tail = None
            self.len = 0
        else:
            node = DequeNode(value)
            self.head = node
            self.tail = node
            self.head.nxt = self.tail
            self.tail.prev = self.head
            self.len = 1

    def push_front(self, value):
        if self.len <= 0:
            node = DequeNode(value)
            self.head = node
            self.tail = node
            self.head.nxt = self.tail
            self.tail.prev = self.head
        else:
            node = DequeNode(value, self.head)
            self.head.prev = node
            self.head = node
        self.len += 1

    def push_back(self, value):
        if self.len <= 0:
            node = DequeNode(value)
            self.head = node
            self.tail = node
            self.head.nxt = self.tail
            self.tail.prev = self.head
        else:
            node = DequeNode(value, None, self.tail)
            self.tail.nxt = node
            self.tail = node
        self.len += 1

    def front(self):
        if self.len <= 0:
            raise IndexError("deque is empty")
        return self.head.value

    def back(self):
        if self.len <= 0:
            raise IndexError("deque is empty")
        return self.tail.value

    def pop_front(self):
        if self.len <= 0:
            raise ValueError("Can not pop from empty deque")
        value = self.front()
        self.head = self.head.nxt
        self.len -= 1
        return value

    def pop_back(self):
        if self.len <= 0:
            raise ValueError("Can not pop from empty deque")
        value = self.tail.value
        self.tail = self.tail.prev
        self.len -= 1
        return value

    def size(self):
        return self.len

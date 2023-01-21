from structures.stack import Stack
import pytest
import random


def test_init():
    string = "something"
    s1, s2 = Stack(), Stack(string)
    assert s1.head is None
    assert s2.head.value == string


def test_push():
    string1 = "something"
    string2 = "else"
    stack = Stack()
    stack.push(string1)
    assert stack.head.value == string1
    assert stack.head.prev is None

    stack.push(string2)
    assert stack.head.value == string2
    assert stack.head.prev is not None


def test_nonempty_top():
    string1 = "something"
    string2 = "else"
    stack = Stack()
    stack.push(string1)
    assert stack.top() == string1
    stack.push(string2)
    assert stack.top() == string2


def test_top_error():
    stack = Stack()
    with pytest.raises(IndexError) as excinfo:
        stack.top()
    assert "empty" in str(excinfo.value).lower()


def test_pop():
    stack = Stack()
    test_objects = [1, "1", 3.14, lambda x: x, list]
    for test_object in test_objects:
        stack.push(test_object)
        assert test_object == stack.pop()


def test_pop_error():
    stack = Stack()
    with pytest.raises(ValueError) as excinfo:
        stack.pop()
    assert "empty" in str(excinfo.value).lower()
    stack.push("x1")
    stack.pop()
    with pytest.raises(ValueError) as excinfo:
        stack.pop()
    assert "empty" in str(excinfo.value).lower()


def test_size():
    for _ in range(100):
        stack = Stack()
        expected_size = random.randint(1, 100)
        for x in range(expected_size):
            stack.push(x)
        assert stack.size() == expected_size
        for _ in range(expected_size):
            stack.pop()
        assert stack.size() == 0

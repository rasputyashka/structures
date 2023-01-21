from structures.queue import Queue
import pytest
import random


def test_init():
    string = "something"
    q1, q2 = Queue(), Queue(string)
    assert q1.head is None
    assert q1.tail is None

    assert q2.head.value == string
    assert q2.tail.value == string


def test_push():
    string1 = "something"
    string2 = "else"
    queue = Queue()
    queue.push(string1)

    assert queue.head.value == string1
    assert queue.tail.value == string1

    queue.push(string2)

    assert queue.head.value == string1
    assert queue.tail.value == string2

    queue_with_init = Queue(string1)
    assert queue_with_init.head.value == string1
    assert queue_with_init.tail.value == string1

    queue_with_init.push(string2)

    assert queue_with_init.head.value == string1
    assert queue_with_init.tail.value == string2


def test_front_only():
    string1 = "a"

    queue = Queue(string1)
    assert queue.front() == string1


def test_front_only_error():
    queue = Queue()
    with pytest.raises(IndexError) as excinfo:
        queue.front()
    assert "empty" in str(excinfo.value).lower()


def test_pop_only():
    string1 = "abc"
    queue = Queue(string1)

    assert queue.pop() == string1


def test_pop_only_error():
    queue = Queue()
    with pytest.raises(ValueError) as excinfo:
        queue.pop()
    assert "empty" in str(excinfo.value).lower()


def test_pop_and_push():
    string1 = "a"
    string2 = "b"
    string3 = "c"

    queue = Queue()
    queue.push(string1)
    assert queue.front() == string1
    queue.push(string2)
    queue.push(string3)

    assert queue.pop() == string1
    assert queue.pop() == string2
    assert queue.pop() == string3


def test_size():
    for _ in range(100):
        q = Queue()
        expected_size = random.randint(1, 100)
        for x in range(expected_size):
            q.push(x)
        assert q.size() == expected_size
        for _ in range(expected_size):
            q.pop()
        assert q.size() == 0

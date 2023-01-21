from structures.deque import Deque
import pytest
import random


def test_init():
    string = "something"
    d1, d2 = Deque(), Deque(string)
    assert d1.head is None
    assert d1.tail is None

    assert d2.head.value == string
    assert d2.tail.value == string


def test_push_back():
    string1 = "something"
    string2 = "else"
    deque = Deque()
    deque.push_back(string1)

    assert deque.tail.value == string1

    deque.push_back(string2)

    assert deque.tail.value == string2

    deque_with_init = Deque(string1)

    assert deque_with_init.tail.value == string1

    deque_with_init.push_back(string2)

    assert deque_with_init.tail.value == string2


def test_front_only():
    string1 = "a"

    deque = Deque(string1)
    assert deque.front() == string1


def test_back_only():
    string1 = "a"

    deque = Deque(string1)
    assert deque.back() == string1


def test_front_only_error():
    deque = Deque()
    with pytest.raises(IndexError) as excinfo:
        deque.front()
    assert "empty" in str(excinfo.value).lower()


def test_back_only_error():
    deque = Deque()
    with pytest.raises(IndexError) as excinfo:
        deque.back()
    assert "empty" in str(excinfo.value).lower()


def test_pop_back_only():
    string1 = "abc"
    deque = Deque(string1)

    assert deque.pop_back() == string1


def test_pop_front_only():
    string1 = "abc"
    deque = Deque(string1)

    assert deque.pop_front() == string1


def test_pop_back_only_error():
    queue = Deque()
    with pytest.raises(ValueError) as excinfo:
        queue.pop_back()
    assert "empty" in str(excinfo.value).lower()


def test_pop_front_only_error():
    queue = Deque()
    with pytest.raises(ValueError) as excinfo:
        queue.pop_front()
    assert "empty" in str(excinfo.value).lower()


def test_pop_front_and_push_back():
    string1 = "a"
    string2 = "b"
    string3 = "c"

    deque = Deque()
    deque.push_back(string1)
    deque.push_back(string2)
    deque.push_back(string3)

    assert deque.pop_front() == string1
    assert deque.pop_front() == string2
    assert deque.pop_front() == string3


def test_pop_back_and_push_front():
    string1 = "a"
    string2 = "b"
    string3 = "c"

    deque = Deque()
    deque.push_front(string1)
    deque.push_front(string2)
    deque.push_front(string3)

    assert deque.pop_back() == string1
    assert deque.pop_back() == string2
    assert deque.pop_back() == string3


def test_pop_back_and_push_back():
    string1 = "a"
    string2 = "b"
    string3 = "c"

    deque = Deque()
    deque.push_back(string1)
    deque.push_back(string2)
    deque.push_back(string3)

    assert deque.pop_back() == string3
    assert deque.pop_back() == string2
    assert deque.pop_back() == string1


def test_pop_front_and_push_front():
    string1 = "a"
    string2 = "b"
    string3 = "c"

    deque = Deque()
    deque.push_front(string1)
    deque.push_front(string2)
    deque.push_front(string3)

    assert deque.pop_front() == string3
    assert deque.pop_front() == string2
    assert deque.pop_front() == string1


def test_several_pops():
    string1 = "a"
    string2 = "b"
    string3 = "c"
    string4 = "d"

    deque = Deque()
    deque.push_front(string1)
    deque.push_back(string2)
    deque.push_front(string3)
    deque.push_back(string4)

    assert deque.pop_back() == string4
    assert deque.pop_front() == string3
    assert deque.pop_front() == string1
    assert deque.pop_front() == string2


def test_size():
    for _ in range(100):
        d = Deque()
        expected_size = random.randint(1, 100)
        for x in range(expected_size):
            d.push_back(x)
        assert d.size() == expected_size
        for _ in range(expected_size):
            d.pop_front()
        assert d.size() == 0

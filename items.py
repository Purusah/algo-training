from typing import Optional, TypeVar, Generic
from dataclasses import dataclass
from collections.abc import Iterator, Sized

T = TypeVar("T")

class EmptyCollection(Exception):
    ...

class FullCollection(Exception):
    ...


@dataclass
class Node(object):
    link: Optional['Node']
    value: T

    def __repr__(self) -> str:
        return f"{self.value} link {self.link}"


class Bag(Iterator):
    def add(self, item: T) -> None:
        ...

    @property
    def size(self) -> int:
        return 0

    @property
    def is_empty(self) -> bool:
        return False


class Queue(Iterator):
    def __init__(self):
        self._len = 0
        self._start: Optional[T] = None
        self._end: Optional[T] = None

    @property
    def size(self) -> int:
        return self._len

    @property
    def is_empty(self) -> bool:
        return not bool(self._len)

    def __len__(self) -> int:
        return self._len

    def enqueue(self, item: T) -> None:
        elem = Node(link=None, value=item)
        if not self._len:
            self._start = elem
        else:
            self._end.link = elem
        self._end = elem
        self._len += 1

    def dequeue(self) -> T:
        if not self._len:
            raise EmptyCollection
        elem = self._start
        self._start = elem.link
        self._len -= 1
        if not self._len:
            self._start = None
            self._end = None
        return elem.value

    def __iter__(self):
         return self

    def __next__(self) -> T:
        try:
            elem = self.dequeue()
        except EmptyCollection:
            raise StopIteration
        else:
            return elem.value

    def __repr__(self) -> str:
        return f"{self._end}"


class Stack(Iterator, Sized):
    def __init__(self):
        self._len = 0
        self._root = None

    @property
    def size(self) -> int:
        return self._len

    @property
    def is_empty(self) -> bool:
        return not bool(self._len)

    def __len__(self) -> int:
        return self._len

    def push(self, item: T) -> None:
        elem = Node(link=self._root, value=item)
        self._root = elem
        self._len += 1

    def pop(self) -> T:
        if not self._len:
            raise EmptyCollection
        elem = self._root
        self._root = elem.link
        self._len -= 1
        return elem.value

    def peek(self) -> T:
        if not self._len:
            raise EmptyCollection
        return self._root.value

    def __iter__(self):
         return self

    def __next__(self):
        try:
            elem = self.pop()
        except EmptyCollection:
            raise StopIteration
        else:
            return elem.value

    def __repr__(self) -> str:
        return f"Stack({self._len}) to {self._root}"


# 1.3.39
class RingBuffer(Iterator, Sized, Generic[T]):  # Iterator

    def __init__(self, cap: int) -> None:
        self._cap = cap
        self._head = 0  # write
        self._tail = 0  # read
        self._size = 0
        self._container = [None for i in range(self._cap)]

        self._full = False

    def __len__(self) -> int:
        return self._size

    @property
    def cap(self) -> int:
        return self._cap

    @property
    def is_empty(self) -> bool:
        return self._size == 0

    @property
    def is_full(self) -> bool:
        return self._size == self._cap

    def reset(self) -> None:
        self._head, self._tail, self._size = 0, 0, 0

    def put(self, item: T) -> None:
        if self.is_full:
            raise FullCollection
        self._size += 1
        self._container[self._head] = item
        if self._head == self._cap - 1:
            self._head = 0
            return
        self._head += 1

    def get(self) -> T:
        if self.is_empty:
            raise EmptyCollection
        self._size -= 1
        value = self._container[self._tail]
        self._container[self._tail] = None
        if self._tail == self._cap - 1:
            self._tail = 0
            return value
        self._tail += 1
        return value

    def __iter__(self):
        return self

    def __next__(self) -> T:
        try:
            value: T = self.get()
        except EmptyCollection:
            raise StopIteration
        return value

    def __str__(self) -> str:
        return f"RingBuffer(size={len(self)}, cap={self._cap}, is_empty={self.is_empty} is_full={self.is_full} collection={self._container})"


if __name__ == "__main__":
    rb = RingBuffer[int](5)
    print(rb)
    try:
        rb.get()
    except EmptyCollection:
        print("RingBuffer empty")
    else:
        raise AssertionError("RingBuffer should be empty")

    value0 = 100
    rb.put(value0)
    assert len(rb) == 1
    print(rb)

    assert rb.get() == value0
    assert rb.is_empty
    assert not rb.is_full
    assert len(rb) == 0

    for i in range(6):
        if i == 5:
            try:
                rb.put(100 + i)
            except FullCollection:
                print(rb)
                break
            else:
                raise AssertionError("RingBuffer should be full")
        rb.put(100 + i)
        print(rb)
    print(rb)
    assert rb.is_empty == False
    assert rb.is_full == True
    assert len(rb) == 5
    for i in range(5):
        rb.get()
        print(rb)
    rb.put(105)
    print(rb)
    rb.get()

    print("#########")
    for i in range(5):
        rb.put(80 + i)
    print(rb)
    for item in rb:
        print(item)
    print(rb)

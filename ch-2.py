from items import Stack, Queue, EmptyCollection


class UnknownItem(Exception):
    ...

brackets_map = {
    "[": "]",
    "(": ")",
    "{": "}",
}

# 1.3.37
def joseph_problem(total: int, number: int) -> int:
    q = Queue()
    for i in range(total):
        q.enqueue(i)
    while len(q) != 1:
        for n in range(1, number + 1):
            current = q.dequeue()
            if n % number == 0:
                break
            q.enqueue(current)
    return q.dequeue()


# 1.3.4
def parentheses(brackets):
    s = Stack()
    keys = set(brackets_map.keys())
    values = set(brackets_map.values())
    for b in brackets:
        if b in keys:
            s.push(b)
            continue
        if b in values:
            try:
                elem = s.pop()
                if brackets_map[elem] != b:
                    return False
                continue
            except EmptyCollection:
                return False
        raise UnknownItem
    if s.is_empty:
        return True
    return False


if __name__ == "__main__":
    assert parentheses("[()]{}{[()()]()}") == True
    assert parentheses("[(])") == False
    assert joseph_problem(7, 2) == 6

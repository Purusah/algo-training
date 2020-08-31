from typing import List, NoReturn, Optional


class Node(object):
    def __init__(self, value: int, order: int) -> NoReturn:
        self.value: int = value
        self.order: int = order
        self.frequency: int = 1
        self.left: Optional[Node] = None
        self.right: Optional[Node] = None

    def __gt__(self, other: "Node") -> bool:
        if self.frequency > other.frequency:
            return True
        elif self.frequency < other.frequency:
            return False
        else:
            if self.order < other.order:
                return True
            else:
                return False

    def set_left(self, node: "Node") -> NoReturn:
        self.left = node

    def set_right(self, node: "Node") -> NoReturn:
        self.right = node

    def get_node(self, value: int) -> Optional["Node"]:
        if value == self.value:
            return self
        elif self.right and value > self.value:
            return self.right.get_node(value)
        elif self.left and value < self.value:
            return self.left.get_node(value)
        return None

    def __repr__(self):
        return f"Node (value, order, frequency): {self.value} {self.order} {self.frequency}"


def append_tree(tree: Node, index: int, value: int) -> None:
    if value < tree.value:
        if tree.left:
            return append_tree(tree.left, index, value)
        else:
            return tree.set_left(Node(value, index))
    elif value > tree.value:
        if tree.right:
            return append_tree(tree.right, index, value)
        else:
            return tree.set_right(Node(value, index))
    else:
        tree.frequency += 1
        return


def print_tree(tree: Node, acc: dict = {},  level: int = 0, skip_print: bool = False):
    if not level:
        acc = {}
    if acc.get(level):
        acc[level].append((tree.value, tree.frequency))
    else:
        acc[level] = [(tree.value, tree.frequency)]

    if tree.left:
        print_tree(tree.left, acc=acc, level=level+1)
    if tree.right:
        print_tree(tree.right, acc=acc, level=level+1)

    return acc


def frequency_sort(items: List) -> List:
    if not items:
        return []
    tree = Node(items[0], 0)

    for ix, val in enumerate(items[1:], 1):
        append_tree(tree, ix, val)

    output = sorted(items, key=lambda x: tree.get_node(x), reverse=True)

    return output


if __name__ == '__main__':
    # These "asserts" are used for self-checking and not for an auto-testing
    assert list(frequency_sort([4, 6, 2, 2, 6, 4, 4, 4])) == [4, 4, 4, 4, 6, 6, 2, 2]
    assert list(frequency_sort(['bob', 'bob', 'carl', 'alex', 'bob'])) == ['bob', 'bob', 'bob', 'carl', 'alex']
    assert list(frequency_sort([17, 99, 42])) == [17, 99, 42]
    assert list(frequency_sort([])) == []
    assert list(frequency_sort([1])) == [1]
    print("Coding complete? Click 'Check' to earn cool rewards!")

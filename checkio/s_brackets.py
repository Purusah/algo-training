import re
import collections

maxsize = 1000
opposite_brackets = {"}": "{", "]": "[", ")": "("}
sub_pattern = r"[0-9\+\-\*\/]"
repl_str = ""

class Stack(collections.UserList):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def empty(self):
        if len(self):
            return False
        else:
            return True

    def put(self, e):
        self.append(e)

    def get(self):
        return self.pop()



def checkio(expression):
    stack = Stack()
    brackets_expression = re.sub(sub_pattern, repl_str, expression)
    print(brackets_expression)
    if not brackets_expression:
        return True

    for i in brackets_expression:
        print(f"i: {i}")
        if stack.empty():
            stack.put(i)
        elif i in opposite_brackets.values():
            stack.put(i)
        else:
            temp = stack.get()
            if temp != opposite_brackets.get(i):
                stack.put(temp)
                stack.put(i)
        print(stack)
    if stack.empty():
        return True
    else:
        return False


#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio("((5+3)*2+1)") == True, "Simple"
    assert checkio("{[(3+1)+2]+}") == True, "Different types"
    assert checkio("(3+{1-1)}") == False, ") is alone inside {}"
    assert checkio("[1+1]+(2*2)-{3/3}") == True, "Different operators"
    assert checkio("(({[(((1)-2)+3)-3]/3}-3)") == False, "One is redundant"
    assert checkio("2+3") == True, "No brackets, no problem"

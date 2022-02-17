class Stack:
    def __init__(self):
        self.stackList = []

    def isEmpty(self):
        return bool(self.stackList)

    def push(self, element):
        self.stackList.append(element)

    def pop(self):
        self.stackList.pop(-1)
        if self.peek() is not False:
            return self.stackList[-1]
        else:
            pass

    def peek(self):
        return self.stackList[-1]

    def size(self):
        return len(self.stackList)


def check(stack):
    stack_list = list(stack)
    s = stack()
    for item in stack_list:
        if item == '(':
            s.push(item)
        elif item == ')':
            if s.peek() is not False:
                s.pop()
            else:
                s.push(item)
        if item == '{':
            s.push(item)
        elif item == '}':
            if s.peek() is not False:
                s.pop()
            else:
                s.push(item)
        if item == '[':
            s.push(item)
        elif item == ']':
            if s.peek() is not False:
                s.pop()
            else:
                s.push(item)
    if s.size() == 0 and s.size() == 0 and s.size() == 0:
        print('Balanced')
    else:
        print('Unbalanced')


if __name__ == '__main__':
    a = "(((([{}]))))"
    b = "[([])((([[[]]])))]{()}"
    c = "{{[()]}}"
    d = "}{}"
    e = "{{[(])]}}"
    f = "[[{())}]"
    check(a)
    print('-'*5)
    check(b)
    print('-'*5)
    check(c)
    print('-'*5)
    check(d)
    print('-'*5)
    check(e)
    print('-'*5)
    check(f)

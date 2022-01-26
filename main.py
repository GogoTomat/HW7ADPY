class Stack:
    def __init__(self):
        self.stackList = []

    def isEmpty(self):
        return bool(self.stackList)

    def push(self, element):
        self.stackList.append(element)

    def pop(self):
        self.stackList.pop(-1)
        return self.stackList[-1]

    def peek(self):
        return self.stackList[-1]

    def size(self):
        return len(self.stackList)


def check(stack):
    stack_list = list(stack)
    rounded = Stack()
    curly = Stack()
    square = Stack()
    for item in stack_list:
        if item == '(':
            rounded.push(item)
        elif item == ')':
            if rounded.peek() is not False:
                rounded.pop()
            else:
                rounded.push(item)
        if item == '{':
            curly.push(item)
        elif item == '}':
            if curly.peek() is not False:
                curly.pop()
            else:
                curly.push(item)
        if item == '[':
            square.push(item)
        elif item == ']':
            if square.peek() is not False:
                square.pop()
            else:
                square.push(item)
    if square.size() == 0 and curly.size() == 0 and rounded.size() == 0:
        print('Balanced')
    else:
        print('Unbalanced')

"""Solution to 3.2 Stack Min from Cracking the Coding Interview"""

class Stack_Min(object):
    def __init__(self):
        self.stack = []
        self.min_stack = []


    # push
    def push(self, x):
        self.stack.append(x)
        # check min
        if not self.min_stack or x <= self.min_stack[-1]:
            self.min_stack.append(x) 

    # pop
    def pop_min(self):
        x = self.stack.pop()
        # check min
        if x == self.min_stack[-1]:
            self.min_stack.pop()
        return x

if __name__ == "__main__":
    stack_with_min = Stack_Min()
    stack_with_min.push(4)
    stack_with_min.push(27)
    stack_with_min.push(4)
    stack_with_min.push(6)
    stack_with_min.push(8)
    stack_with_min.push(2)
    stack_with_min.push(17)
    stack_with_min.push(2)
    stack_with_min.push(24)

    print "This is stack:", stack_with_min.stack
    print "This is min_stack:", stack_with_min.min_stack

    while stack_with_min.stack:
        print "Popping ...", stack_with_min.pop_min()
        print "This is min_stack:", stack_with_min.min_stack
import sys


class stack:
    def __init__(self):
        self.stack = list()

    def push(self,x):
        self.stack.append(x)

    def pop(self):
        if not self.stack:
            return -1
        return self.stack.pop()

    def size(self):
        return len(self.stack)

    def empty(self):
        if len(self.stack) == 0:
            return 1
        else:
            return 0

    def top(self):
        if not self.stack:
            return -1
        return self.stack[-1]

    def run(self):
        n = int(sys.stdin.readline())
        for _ in range(n):
            data = list(map(str,sys.stdin.readline().split()))
            cmd = data[0]
            if cmd == 'push':
                self.push(int(data[1]))
            elif cmd == 'top':
                print(self.top())
            elif cmd == 'size':
                print(self.size())
            elif cmd == 'empty':
                print(self.empty())
            elif cmd == 'pop':
                print(self.pop()) 

s = stack()
s.run()

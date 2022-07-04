import sys
from collections import deque


class queue:
    def __init__(self):
        self.queue = deque()

    def push(self,x):
        self.queue.append(x)

    def pop(self):
        if not self.queue:
            return -1
        return self.queue.popleft()

    def size(self):
        return len(self.queue)

    def empty(self):
        if len(self.queue) == 0:
            return 1
        else:
            return 0

    def back(self):
        if not self.queue:
            return -1
        return self.queue[-1]

    def front(self):
        if not self.queue:
            return -1
        return self.queue[0]

    def run(self):
        n = int(sys.stdin.readline())
        for _ in range(n):
            data = list(map(str,sys.stdin.readline().split()))
            cmd = data[0]
            if cmd == 'push':
                self.push(int(data[1]))
            elif cmd == 'pop':
                print(self.pop())
            elif cmd == 'size':
                print(self.size())
            elif cmd == 'empty':
                print(self.empty())
            elif cmd == 'front':
                print(self.front())
            elif cmd == 'back':
                print(self.back()) 

s = queue()
s.run()

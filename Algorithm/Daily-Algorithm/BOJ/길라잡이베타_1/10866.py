import sys


class Deque:
    def __init__(self):
        self.deque = []

    def push_back(self, num):
        self.deque.append(num)

    def push_front(self, num):
        self.deque = [num] + self.deque

    def pop_front(self):
        try:
            front = self.deque.pop(0)
            return front
        except IndexError:
            return -1

    def pop_back(self):
        try:
            back = self.deque.pop()
            return back
        except IndexError:
            return -1

    def size(self):
        return len(self.deque)

    def empty(self):
        if self.deque:
            return 0
        else:
            return 1

    def front(self):
        try:
            return self.deque[0]
        except:
            return -1

    def back(self):
        try:
            return self.deque[-1]
        except:
            return -1

    def run(self):
        n = int(sys.stdin.readline())
        for _ in range(n):
            s_li = list(map(str,sys.stdin.readline().strip().split()))

            if s_li[0] == 'push_back':
                self.push_back(int(s_li[1]))
            elif s_li[0] == 'push_front':
                self.push_front(int(s_li[1]))
            elif s_li[0] == 'pop_front':
                print(self.pop_front())
            elif s_li[0] == 'pop_back':
                print(self.pop_back())
            elif s_li[0] == 'size':
                print(self.size())
            elif s_li[0] == 'empty':
                print(self.empty())
            elif s_li[0] == 'front':
                print(self.front())
            elif s_li[0] == 'back':
                print(self.back())


deque = Deque()
deque.run()

class Deque:
    def __init__(self):
        self.deque = []
    def append_front(self, x):
        self.deque.insert(0, x)

    def pop_front(self):
        self.deque.pop(0)

    def append_rear(self, x):
        self.deque.append(x)

    def pop_rear(self):
        self.deque.pop()

    def lenD(self):
        print(len(self.deque))

    def is_empty(self):
        print(len(self.deque) == 0)

    def clear(self):
        self.deque.clear()
    def show(self):
        print(self.deque)

if __name__=='__main__':
    a = Deque()
    a.append_front(2)
    a.show()
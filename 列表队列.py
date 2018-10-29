
class Queue:
    def __init__(self):
        self.queue = []
    def enQ(self,x):
        self.queue.append(x)
    def deQ(self):
        if len(self.queue)==0:
            print('cannot pop from an empty queue.')
        else:
            print('Remove:%s'%self.queue.pop(0))
    def sizeQ(self):
        print(len(self.queue))
    def show(self):
        print(self.queue)
    def emptyQ(self):
        print(len(self.queue) == 0)
if __name__=='__main__':
    a = Queue()
    a.enQ(5)
    a.enQ(7)
    a.enQ(1)
    a.deQ()
    a.show()
    a.emptyQ()
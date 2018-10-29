import heapq
class PriorityQueue:
    def __init__(self):
        self.queue=[]
        self.index=0
    def push(self,item,priority):
        heapq.heappush(self.queue,(-priority,self.index,item))
        self.index+=1
    def pop(self):
        print(heapq.heappop(self.queue)[-1])
q=PriorityQueue()
q.push('foo',1)
q.push('jii',5)
q.push('boo',4)
q.pop()
class Node(object):
    def __init__(self,val,p=0):
        self.data = val
        self.next = p

class LinkList(object):
    def __init__(self):
        self.head = 0
    def initstr(self,data):
        self.head = Node(int(data[0]))
        p = self.head
        for i in data[1:]:
            node = Node(int(i))
            p.next = node
            p = p.next
    def initlist(self,data):
        self.head = Node(data[0])
        p = self.head
        for i in data[1:]:
            node = Node(i)
            p.next = node
            p = p.next
    def getlength(self):
        p =  self.head
        length = 0
        while p!=0:
            length+=1
            p = p.next
        return length
    def is_empty(self):
        if self.getlength() ==0:
            return True
        else:
            return False
    def clear(self):
        self.head = 0
    def append(self,item):
        q = Node(item)
        if self.head ==0:
            self.head = q
        else:
            p = self.head
            while p.next!=0:
                p = p.next
            p.next = q
    def getitem(self,index):
        if self.is_empty():
            print('Linklist is empty.')
            return
        j = 0
        p = self.head
        while p.next!=0 and j <index:
            p = p.next
            j+=1
        if j ==index:
            return p.data
        else:
            print('target is not exist!')
    def insert(self,index,item):
        p = self.head
        post  = self.head
        j = 0
        while p.next!=0 and j<index:
            post = p
            p = p.next
            j+=1
        if index ==j:
            q = Node(item,p)
            post.next = q
            q.next = p
    def delete(self,index):
        p = self.head
        post  = self.head
        j = 0
        while p.next!=0 and j<index:
            post = p
            p = p.next
            j+=1
        if index ==j:
            post.next = p.next
    def index(self,value):
        if self.is_empty():
            print('Linklist is empty.')
            return
        p = self.head
        i = 0
        while p.next!=0 and not p.data ==value:
            p = p.next
            i+=1
        if p.data == value:
            return i
        else:
            return -1
    def findnode(self,index):
        """思路是设置两个指针，分别为 ahead, behind，前指针先走
        k-1 步，然后 ahead 和 behind 同步向后走，直到 ahead
        走到最后，此时 behind 所在的位置就是倒数第 k 个节点了。
        考虑边界条件：
        1. 空链表
        2. k 为 0
        3. total_length < k
        """
        if self.head is None:
            return None
        if index < 1:
            return None
        behind, ahead = self.head, self.head
        for _ in range(index - 1):
            # 头指针先走 k -1 步
            ahead = ahead.next
            if ahead is None:
                # 防止走过头了，可能链表长度不够
                return None
        # 前后指针共同往后走
        while ahead.next:
            ahead = ahead.next
            behind = behind.next
        # behind 所指向的就是相应的节点
        return behind.data
    def show(self):
        p = self.head
        while p != 0:
            print(p.data,end = ' ')
            p = p.next
        print()
    def resverselist1(self):#链表倒序
        if self.head is None :
            return None
        p = self.head
        nodes = []
        while p != 0:
            nodes.append(p.data)
            p = p.next
        while len(nodes) > 0:
            print(nodes.pop(), end='')

# #两个长整型相加
# l = LinkList()
# m = LinkList()
# n = LinkList()
# l.initstr('1000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
# m.initstr('1000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
# a = l.getlength()-1
# b = m.getlength()-1
# JW = 0
# x = l.getitem(a)+m.getitem(b)
# a = a-1
# b = b-1
# y = x%10
# n.append(y)
# if x>9:
#     JW = 1
# BOOL = True
# while BOOL:
#     while b>=0:
#         x = l.getitem(a) + m.getitem(b)
#         y = x % 10
#         n.append(y+JW)
#         if x>9:
#             JW = 1
#         else:
#             JW = 0
#         a -= 1
#         b -= 1
#     if a == -1:
#         break
#     c = l.getitem(a)+JW
#     d = c % 10
#     n.append(d)
#     if c >9:
#         JW = 1
#     else:
#         JW = 0
#     a -= 1
# if JW == 1:
#     n.append(1)
# n.resverselist1()
#两升序链表合并为一个降序链表
l = LinkList()
m = LinkList()
n = LinkList()
l.initlist([5,10,15])
m.initlist([6,7,10,20,25])
a = m.getlength()-1
b = l.getlength()-1
while b >=0:
    while a >= 0 and m.getitem(a)>l.getitem(b):
        n.append(m.getitem(a))
        m.delete(a)
        a -= 1
    else:
        n.append(l.getitem(b))
        l.delete(b)
    b -= 1
n.show()

# 给定两个非空链表来代表两个非负整数，
# 位数按照逆序方式存储，
# 它们的每个节点只存储单个数字。
# 将这两数相加会返回一个新的链表。
class ListNode(object):

    def __init__(self, x):
        self.val = x
        self.next = None

class Link(object):

    def __init__(self):
        self.head = None
        self.size = 0

    def isEmpty(self):
        return self.head == None

    def length(self):
        current = self.head
        count = 0
        while current != None:
            count += 1
            current = current.next
        return count

    def initlist(self, data):
        self.head = ListNode(data[0])
        p = self.head
        for i in data[1:]:
            node = ListNode(i)
            p.next = node
            p = p.next

    def append(self, val):
        temp = ListNode(val)
        if self.isEmpty():
            self.head = temp
        else:
            current = self.head
            while current.next != None:
                current = current.next
            current.next = temp

    def add(self, val):
        temp = ListNode(val)
        if self.isEmpty():
            self.head = temp
        else:
            temp.next = self.head
            self.head = temp

    def popp(self, index):
        current1 = self.head
        current2 = self.head
        j = 0
        while current1.next != None and j < index:
            current2 = current1
            current1 = current1.next
            j += 1
        if j == index:
            current2.next = current1.next

    def printf(self):
        rlist = []
        if self.isEmpty():
            print("NONE")
        else:
            current = self.head
            while current != None:
                rlist.append(current.val)
                current = current.next
            print(rlist, end="")

class Solution(object):

    def length(self, l):
        current = l
        count = 0
        while current != None:
            count += 1
            current = current.next
        return count

    def addTwoNumbers(self, l1, l2):
        rList = Link()
        if self.length(l1) >= self.length(l2):
            current1 = l1
            current2 = l2
            count = self.length(l2)
        else:
            current2 = l1
            current1 = l2
            count = self.length(l1)
        zCount = 0
        addFlag = 0
        while current1 != None:
            tempVal = current1.val
            if zCount < count:
                tempVal = tempVal + current2.val
                current2 = current2.next
            if addFlag > 0:
                tempVal = tempVal + addFlag
                addFlag = 0
            if tempVal >= 10:
                tempVal = tempVal - 10
                addFlag = 1
            rList.append(tempVal)
            current1 = current1.next
            zCount = zCount + 1
        if addFlag > 0:
            rList.append(addFlag)
        return rList

if __name__ == '__main__':
    ll1 = Link()
    ll1.initlist([2, 4, 3])
    ll2 = Link()
    ll2.initlist([5, 6, 4])
    l1 = ll1.head
    l2 = ll2.head
    rl = Solution().addTwoNumbers(l1, l2)
    rl.printf()
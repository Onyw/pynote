class Stack:
    def __init__(self):
        self.stack = []
    def pushlist(self,str):
        for i in range(len(str)):
            self.stack.append(str[i])
    def pushS(self,x):
        self.stack.append(x)
    def popit(self):
        if len(self.stack) == 0:
            print('cannot pop from an empty stack.')
        else:
            print('Remove:%s'%self.stack.pop())
    def viewstack(self):
        print(self.stack)
    def empytS(self):
        return len(self.stack) == 0
    def lenS(self):
        return len(self.stack)
    def clear(self):
        self.stack.clear()
if __name__=='__main__':
    #小括号中括号大括号匹配
    # a = Stack()
    # b = input()
    # c = len(b)
    # if c % 2 != 0:
    #     print("Invalid")
    # else:
    #     for i in range(c):
    #         if b[i] == '{' or b[i] == '[' or b[i] == '(':
    #             a.pushS(b[i])
    #         elif b[i] == '}':
    #             if a.stack[-1] != '{':
    #                 print("Invalid")
    #                 break
    #             else:
    #                 a.popit()
    #         elif b[i] == ']':
    #             if a.stack[-1] != '[':
    #                 print("Invalid")
    #                 break
    #             else:
    #                 a.popit()
    #         elif b[i] == ')':
    #             if a.stack[-1] != '(':
    #                 print("Invalid")
    #                 break
    #             else:
    #                 a.popit()
    #     if a.empytS():
    #         print("valid")
    #利用栈找出最小元素
    a = Stack()
    c = [7,5,4,6,2,1]
    a.pushlist(c)
    min = a.stack[-1]
    for i in range(a.lenS()):
        if a.stack[-1] < min:
            min = a.stack[-1]
            a.popit()
        else:
            a.popit()
    print(min)
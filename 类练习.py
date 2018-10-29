####1.定义类并创建类的对象
##class Person(object):
##    pass
####2.创建实例
##xiaoming=Person()
####3.创建实例属性
##xiaoming.age='10'
##xiaoming.name='QQ'
####4.初始化实例属性__init__(self)
##class Person(object):
##    def __init__(self,name,age,sex):
##       self.name=name
##       self._sex=sex
##       self.__age=age
####5.访问权限
##xxx 公有成员
##_xxx 受保护成员
##__xxx 私有成员
####6.增加类属性+调用次数
##class Person(object):
##    nationality='china'
##    sum=0
##    def __init__(self,name,age,sex):
##       self.name=name
##       self._sex=sex
##       self.__age=age
##       Person.sum+=1
##       print(Person.sum)
####7.练习
##class student(object):
##    def __init__(self,name,score):
##         self.name=name
##         self.__score=score
##    def get_score(self):
##        if self.__score<60:
##            return 'c'
##        if 60<=self.__score<90:
##            return 'b'
##        if self.__score>=90:
##            return 'a'
class A(object):
    def show(self):
        print("A")

class B(object):
    def show(self):
        print("B")

class C(A, B):
    def show(self):
        print(self.__class__.mro())
        super(C, self).show()

C().show()
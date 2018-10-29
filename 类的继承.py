class Person(object):

    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.weight = 'weight'

    def talk(self):
        print("person is talking....")


class Chinese(Person):

    def __init__(self, name, age, language):
        Person.__init__(self, name, age)
        self.language = language
        print(self.name, self.age, self.weight, self.language)

    def talk(self):  # 子类 重构方法
        print('%s is speaking chinese' % self.name)

    def walk(self):
        print('is walking...')


c = Chinese('bigberg', 22, 'Chinese')
c.talk()


class SchoolMember(object):
    '''学习成员基类'''
    member = 0

    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex
        self.enroll()

    def enroll(self):
        '注册'
        print('just enrolled a new school member [%s].' % self.name)
        SchoolMember.member += 1

    def tell(self):
        print('----%s----' % self.name)
        for k, v in self.__dict__.items():
            print(k, v)
        print('----end-----')


class Teacher(SchoolMember):
    '教师'

    def __init__(self, name, age, sex, salary, course):
        SchoolMember.__init__(self, name, age, sex)
        self.salary = salary
        self.course = course

    def teaching(self):
        print('Teacher [%s] is teaching [%s]' % (self.name, self.course))


class Student(SchoolMember):
    '学生'

    def __init__(self, name, age, sex, course, tuition):
        SchoolMember.__init__(self, name, age, sex)
        self.course = course
        self.tuition = tuition
        self.amount = 0

    def pay_tuition(self, amount):
        print('student [%s] has just paied [%s]' % (self.name, amount))
        self.amount += amount


t1 = Teacher('Wusir', 28, 'M', 3000, 'python')
t1.teaching()
t1.tell()
s1 = Student('haitao', 38, 'M', 'python', 30000)
s1.pay_tuition(100)
s1.tell()
s2 = Student('lichuang', 12, 'M', 'python', 11000)
s2.pay_tuition(1000)
s2.tell()
print(SchoolMember.member)
# del s2


class A:
    def test(self):
        print("test from A")

class B(A):
    # def test(self):
    #     print("test from B")
    pass

class C(A):
    def test(self):
        print("test from C")

class D(B):
    # def test(self):
    #     print("test from D")
    pass

class E(C):
    def test(self):
        print("test from E")

class F(D,E):
    # def test(self):
    #     print("test from F")
    pass

f1=F()
f1.test()
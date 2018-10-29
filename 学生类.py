class student(object):
    def __init__(self, name,age,grade=[0,0,0]):
        self.name=name
        self.age=age
        self.grade=grade
    @property
    def get_name(self):
        print(str(self.name))
    @property
    def get_age(self):
        print(int(self.age))
    @property
    def get_grade(self):
        if self.grade[0]<self.grade[1]:
            m=self.grade[1]
        else:
            m=self.grade[0]
        if m<self.grade[2]:
            n=self.grade[2]
        else:
            n=m
        print(int(n))
zm=student('zhangming',20,[69,88,90])
zm.get_name
zm.get_age
zm.get_grade

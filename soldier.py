class Gun:
    def __init__(self, model):
        #1.枪类型
        self.model = model
        #2.子弹数量
        self.bullet_count = 0

    def add_bllet(self, count):
        self.bullet_count += count

    def shoot(self):
        #1.判断子弹数量
        if self.bullet_count <= 0:
            print("[%s]没有子弹了" % self.model)
            return
        #2.发射子弹 -1
        self.bullet_count -= 1
        #3.提示发射信息
        print("[%s] biubiubiu... [%d]" % (self.model, self.bullet_count))

class Soldier:
    def __init__(self, name):
        self.name = name
        self.gun = None

    def fire(self):
        #1.判断是否有枪
        if self.gun is None:
            print("[%s]还没有枪" % self.name)
            return
        #2.装弹
        self.gun.add_bllet(50)
        #3.高喊口号
        print("冲啊！[%s]" % self.name)
        #4.发射
        for i in range(self.gun.bullet_count):
            self.gun.shoot()

ak47 = Gun("AK47")
a = Soldier("许三多")
a.gun = ak47
a.fire()
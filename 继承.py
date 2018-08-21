class Animal:
    def eat(self):
        print("eat")

    def drink(self):
        print("drink")

    def run(self):
        print("run")

    def sleep(self):
        print("sleep")

class dog(Animal):
    def bark(self):
        print("Wwwww~")

    def sleep(self):
        super().sleep()
        print("Huhhuu~")


wangcai = Animal()

wangcai.eat()
wangcai.drink()
wangcai.run()
wangcai.sleep()

w = dog()
w.bark()
w.eat()
w.sleep()
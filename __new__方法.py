class MusicPlayer(object):
    #记录第一个创建对象的引用
    instance = None
    #记录是否执行过初始化
    init_flag = False

    def __new__(cls, *args, **kwargs):
        #1.判断类属性是否是空对象
        if cls.instance is None:
            #2.调用父类的方法，为第一个对象分配空间
            cls.instance = super().__new__(cls)
        #3.返回对象的引用
        return cls.instance

    def __init__(self):
        #1.判断是否执行过初始化动作
        if MusicPlayer.init_flag is True:
            return
        #2.如果没执行在执行初始化动作
        print("播放器初始化")
        #3.修改雷属性标记
        MusicPlayer.init_flag = True

player1 = MusicPlayer()
print(player1)
player2 = MusicPlayer()
print(player2)
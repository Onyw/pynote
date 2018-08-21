class Game(object):
    #历史最高分（类属性）
    top_score = 0
    #实例属性
    def __init__(self, name):
        self.player_name = name
    #静态方法
    @staticmethod
    def show_help():
        print("帮助信息：自己想。")
    #类方法
    @classmethod
    def show_top_score(cls):
        print("历史纪录 %d" % cls.top_score)
    #实例方法
    def start_game(self):
        print("%s 开始游戏。。。" % self.player_name)

Game.show_help()
Game.show_top_score()
game = Game("小明")
game.start_game()
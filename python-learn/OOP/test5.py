# Game类设计
import random

class Game:
    top_score=0

    def __init__(self,player_name):
        self.player_name=player_name

    def start_name(self):
        score_now=random.randint(1,10)
        print('%s正在玩游戏，得分为%d' %(self.player_name,score_now))
        if score_now>Game.top_score:
            Game.top_score=score_now

    @classmethod
    def show_top_score(cls):
        print('当前的最高分为%d' %cls.top_score)

    @staticmethod
    def show_help():
        print('该游戏版本1.0')

def main():
    Game.show_help()
    player1=Game('小明')
    player2=Game('小红')
    player3=Game('小李')
    player1.start_name()
    player2.start_name()
    player3.start_name()
    Game.show_top_score()

if __name__=='__main__':
    main()



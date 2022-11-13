# 音乐播放器--单例方法设计
class MusicPlayer(object):
    isinstance=None
    init_flag=False

    def __init__(self):
        if MusicPlayer.init_flag:
            return
        print('播放器初始化')
        MusicPlayer.init_flag=True

    def __new__(cls,*args,**kwargs):
        #print('创建对象，分配空间')
        if cls.isinstance is None:
            cls.isinstance=super().__new__(cls)
            return cls.isinstance
        else:
            return cls.isinstance


player1=MusicPlayer()
print(player1)
player2=MusicPlayer()
print(player2)

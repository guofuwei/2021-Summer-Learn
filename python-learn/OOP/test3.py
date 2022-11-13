# 士兵突击
import random
class Soldier:
    def __init__(self,name,gun):
        self.name=name
        self.gun=gun
    
    def fire(self):
        print('士兵%s扣动扳机' %self.name)
        self.gun.loading(random.randint(1,10))
        self.gun.fire()

class Gun:
    def __init__(self,name):
        self.name=name
        self.nums=0

    def fire(self):
        if self.nums>0:
            self.nums-=1
            print('%s突突突...[%s]' %(self.name,self.nums))

        else:
            print('%s子弹不足，无法开火' %self.name)

    def loading(self,count):
        print('%s正在装填子弹[%s]' %(self.name,count))
        self.nums+=count

def main():
    gun=Gun('AK-47')
    soldier=Soldier('许三多',gun)
    soldier.fire()

if __name__=='__main__':
    main()
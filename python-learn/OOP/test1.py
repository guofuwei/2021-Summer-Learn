# 小明爱跑步
class Person:
    def __init__(self,name,weight):
        self.name=name
        self.weight=weight

    def __str__(self):
        return '%s的体重为%skg' %(self.name,self.weight)

    def run(self):
        self.weight-=2

    def eat(self):
        self.weight+=1

def main():
    xiaoming=Person('小明',75.0)
    xiaoming.run()
    xiaoming.eat()
    print(xiaoming)
    print(__name__)

if __name__=='__main__':
        main()

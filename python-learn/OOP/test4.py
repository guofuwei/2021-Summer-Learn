# 继承
class Animal(object):
    count=0
    def __init__(self):
        self.num1=100
        self._num2=200
        Animal.count+=1
    def _test(self):
        print('test')

    @classmethod
    def change_count(cls,num):
        cls.count=num

class Dog(Animal):
    def bark(self):
        print('汪汪汪')

class XiaoTianQuan(Dog):
    def bark(self):
        super().bark()
        print('$$$$$')

xiaotianquan=XiaoTianQuan()
cat=Animal()
cat.change_count(8)
#print(Animal.count)
xiaotianquan.bark()
#print(xiaotianquan._num2)
#xiaotianquan._test()
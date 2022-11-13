# 用类对函数进行装饰

class Test(object):
    def __init__(self,func):
        self.func=func
    def __call__(self):
        print('这里是装饰器添加的功能')
        self.func()

@Test #相当于get_str=Test(get_str)创建了一个实例对象
def  get_str():
    print('Hello')

get_str() #  调用实例对象的__call__方法
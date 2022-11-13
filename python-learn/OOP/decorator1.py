# 装饰器的实现原理

def set_func(func):
    def call_func():
        print('---这里是权限验证---')
        func()
    return call_func

@set_func #  等价于test1=set_func(test1)
def test1():
    print('---test1---')

# test1=set_func(test1)
test1()

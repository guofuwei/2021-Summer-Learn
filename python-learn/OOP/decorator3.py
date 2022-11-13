# 装饰器的参数传递

def set_func(func):
    print('开始进行装饰')
    def call_func(a):
        print('---这里是权限验证---')
        func(a)
    return call_func

@set_func #  等价于test1=set_func(test1)
def test1(num):
    print('---test1---%d' %num)

# test1=set_func(test1)
# test1(100)

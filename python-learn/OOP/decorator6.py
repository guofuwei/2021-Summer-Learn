# 多个装饰器装饰一个函数

def set_func1(func):
    print('开始进行装饰1')
    def call_func(*args,**kwargs):
        print('---这里是权限验证1---')
        return func(*args,**kwargs)
    return call_func

def set_func2(func):
    print('开始进行装饰2')
    def call_func(*args,**kwargs):
        print('---这里是权限验证2---')
        return func(*args,**kwargs)
    return call_func

@set_func1
@set_func2
def test1():
    print('---test1---')
    return 'ok'

test1()

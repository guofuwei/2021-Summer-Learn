# 装饰器的返回值
#该实例为通用装饰器

def set_func(func):
    print('开始进行装饰')
    def call_func(*args,**kwargs):
        print('---这里是权限验证---')
        return func(*args,**kwargs)
    return call_func

@set_func #  等价于test1=set_func(test1)
def test1(num,*args,**kwargs):
    print('---test1---%d' %num)
    print('---test1---',args)
    print('---test1---',kwargs)
    return 'ok'

# test1=set_func(test1)
test1(100)

# 带有参数的装饰器

def set_level(level_num):
    def set_func(func):
        def call_func(*args,**kwargs):
            if level_num==1:
                print('---权限验证1---')
            elif level_num==2:
                print('---权限验证2---')
            return func()
        return call_func
    return set_func

@set_level(1)#1.将1传入set_level()中，将该函数返回值(set_func)装饰test1  2.test1=set_func(test1)
def test1():
    print('---test1---')  
    return 'ok'

@set_level(2)
def test2():
    print('---test2---')
    return 'okok'

test1()
test2()
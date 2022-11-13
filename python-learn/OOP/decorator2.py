# 装饰器的作用
import time

def set_func(func):
    def call_fun():
        start_time=time.perf_counter()
        func()
        stop_time=time.perf_counter()
        print('程序运行时间为:%.6fs' %(stop_time-start_time))
    return call_fun

@set_func
def test1():
    for i in range(1000000):
        pass

test1()
# generator_process1.py
import time

def task1():
    while True:
        print('---1---')
        time.sleep(0.2)
        yield
    
def task2():
    while True:
        print('---2---')
        time.sleep(0.2)
        yield

def main():
    t1=task1()
    t2=task2()
    while True:
        next(t1)
        next(t2)
# 交替进行为并发，是'假的'并行
if __name__=='__main__':
    main()
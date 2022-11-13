# Fibgenerator.py

from typing import ForwardRef


def Fibgenerator(n):
    num1=0
    num2=1
    current_num=0
    while current_num<n:
        num1,num2=num2,num1+num2
        current_num+=1
        ret=yield num1  #  如果一个函数中有yield，那么这个函数就用来产生生成器
        print('ret>>',ret)
    return 'done'

Fib = Fibgenerator(1)
print(Fib.send(None))


while True:
    try:
        ret=Fib.send('haha')
        print(ret)
    except StopIteration:
        break
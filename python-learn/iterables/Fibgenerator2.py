# Fibgenerator.py

from typing import ForwardRef


def Fibgenerator(n):
    num1=0
    num2=1
    current_num=0
    while current_num<n:
        num1,num2=num2,num1+num2
        current_num+=1
        yield num1  #  如果一个函数中有yield，那么这个函数就用来产生生成器
    return 'done'

Fib = Fibgenerator(10)
print(Fib)

while True:
    try:
        ret=next(Fib)
        print(ret)
    except Exception as ret:
        print(ret.value)
        break
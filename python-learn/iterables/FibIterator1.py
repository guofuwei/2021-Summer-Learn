# FibIterator1.py

import time
class FibIterator(object):
    def __init__(self,n):
        self.n=n
        self.current=0
        self.num1=0
        self.num2=1
    def __iter__(self):
        return self
    def __next__(self):
        if  self.current<self.n:
            self.num2,self.num1=self.num1+self.num2,self.num2
            self.current+=1
            return self.num1
        else:
            raise StopIteration

Fib_test=FibIterator(30)
for i in Fib_test:
    print(i,end=',')

from collections import Iterable
from collections import Iterator
import time

class Classmate(object):
    def __init__(self):
        self.names=list()
        self.current_num=0
    def add(self,name):
        self.names.append(name)
    def __iter__(self):
        return self
    def __next__(self):
        if self.current_num<len(self.names):
            ret=self.names[self.current_num]
            self.current_num+=1
            return ret
        else:
            raise StopIteration

classmate=Classmate()
classmate.add('王二')
classmate.add('张三')
classmate.add('李四')

#print('判断classmate是否可以迭代:',isinstance(classmate,Iterable))
#classiterator=iter(classmate)
#print('判断classiterator是否为迭代器:',isinstance(classiterator,Iterator))

for i in classmate:
    print(i)
    time.sleep(1)

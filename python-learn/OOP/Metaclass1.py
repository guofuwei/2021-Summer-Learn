# 元类的使用

class A(object):
    num=100

def print_b(self):
    print(self.num)

@staticmethod
def print_static():
    print('---hahaha---')

@classmethod
def print_class(cls):
    print(cls.num)

B=type('B',(A,),{'print_b':print_b,'print_static':print_static,
    'print_class':print_class})
b=B()
print(help(B))
b.print_b()
b.print_static()
b.print_class()


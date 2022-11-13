# 利用元类将类中的所有变量大写

def upper_attr(class_name,class_parent,class_attr): #相当于传入('Foo',(object,),('bar':'bip'))
    new_attr={}
    for name,value in class_attr.items():
        if not name.startswith('__'):
            new_attr[name.upper()]=value
    
    return type(class_name,class_parent,new_attr)

class Foo(object,metaclass=upper_attr):
    bar='bip'

print(hasattr(Foo,'bar'))
print(hasattr(Foo,'BAR'))

f=Foo()
print(f.BAR)
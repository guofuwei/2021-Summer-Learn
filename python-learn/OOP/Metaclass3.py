# 利用元类将类中的所有变量大写

class UpperAttrMetaClass(type):
    def __new__(cls,class_name,class_parents,class_attr):
        new_attr={}
        for name,value in class_attr.items():
            if not name.startswith('__'):
                new_attr[name.upper()]=value
        
        return type(class_name,class_parents,new_attr)

class Foo(object,metaclass=UpperAttrMetaClass):
    bar='bip'

print(hasattr(Foo,'bar'))
print(hasattr(Foo,'BAR'))

f=Foo()
print(f.BAR)
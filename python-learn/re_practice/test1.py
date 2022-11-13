import re

def main():
    names=['_age','age','1age','___age','age#','age55']
    for name in names:
        ret=re.match(r'^[_a-zA-Z]\w*$',name)
        if ret:
            print('变量%s符合要求,通过正则匹配的是%s' %(name,ret.group()))
        else:
            print('变量%s不符合要求' %name)

if __name__=='__main__':
    main()
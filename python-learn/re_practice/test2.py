import re

def main():
    email=input('请输入一个邮箱地址:')
    # 如果在正则表达式中要使用一些普通符号，例如?,.等请在其前面加上转移符号
    ret=re.match(r'[0-9a-zA-Z_]{4,20}@(163|126)\.com$',email)
    if ret:
        if ret.group(1)=='163':
            print('该邮箱是一个163邮箱')
        else:
            print('该邮箱是一个126邮箱')
    else:
        print('该邮箱不是一个邮箱地址')

if __name__=='__main__':
    main()

#  re.match(r'<(\w*)>.*</\1>',html_str)
# 补充知识，可以用分组的方式去成对匹配html的标签
# re.match(r'<(?P<p1>\w*)><(?P<p2>\w*)>.*</(?P=p2)></(?P=p1)>',html_str)
# 使用?P=<name>可以给分组起一个别名，方便使用
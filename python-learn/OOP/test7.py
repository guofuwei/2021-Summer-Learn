# 异常的传递,异常的主动抛出

def input_pwd():
    pwd=input('请输入密码:')
    if len(pwd)>=8:
        return pwd
    else:
        raise Exception('密码长度不够')

def main():
    try:
        pwd=input_pwd()
        print(pwd)
    except Exception as ret:
        print(ret)

if __name__=='__main__':
    main()

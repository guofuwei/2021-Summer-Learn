try:
    num=int(input('请输入一个整数:'))
    result=8/num
except ZeroDivisionError:
    print('除0错误')
except ValueError:
    print('输入的不是一个整数')
except Exception as ret:
    print(ret)
else:
    print('结果为:'+str(result))
finally:
    print('程序运行完毕')
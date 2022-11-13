# 闭包
def line(k,b):
    def create_y(x):
        print(k*x+b)
    return create_y

line1=line(1,2)
line1(1)
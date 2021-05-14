import itertools

def pi(N):
    ' 计算pi的值 '
    # step 1: 创建一个奇数序列: 1, 3, 5, 7, 9, ...
    odd = itertools.count(1,2)
    # step 2: 取该序列的前N项: 1, 3, 5, 7, 9, ..., 2*N-1.
    l = list(itertools.takewhile(lambda x:x<=2*N-1,odd))
    # step 3: 添加正负符号并用4除: 4/1, -4/3, 4/5, -4/7, 4/9, ...
    sum=0
    n=1
    for i in l:
        if n%2==1:
            sum+=(4/i)
        else:
            sum+=(-4/i)
        n=n+1
    # step 4: 求和:
    return sum

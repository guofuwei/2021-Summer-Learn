import gevent
import time

def f1(n):
    for i in range(n):
        print(gevent.getcurrent(),i)
        gevent.sleep(0.5)

def f2(n):
    for i in range(n):
        print(gevent.getcurrent(),i)
        gevent.sleep(0.5)

def f3(n):
    for i in range(n):
        print(gevent.getcurrent(),i)
        gevent.sleep(0.5)

def main():
    print('---1---')
    g1=gevent.spawn(f1,5)
    g2=gevent.spawn(f2,5)
    g3=gevent.spawn(f3,5)
    print('---2---')
    g1.join()
    g2.join()
    g3.join()

if __name__=='__main__':
    main()

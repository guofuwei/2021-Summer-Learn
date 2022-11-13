from gevent import monkey
monkey.patch_all()
import gevent

import time



def f1(n):
    for i in range(n):
        print(gevent.getcurrent(),i)
        time.sleep(0.5)

def f2(n):
    for i in range(n):
        print(gevent.getcurrent(),i)
        time.sleep(0.5)

def f3(n):
    for i in range(n):
        print(gevent.getcurrent(),i)
        time.sleep(0.5)

def main():
    gevent.joinall([
        gevent.spawn(f1,5),
        gevent.spawn(f2,5),
        gevent.spawn(f3,5)
    ])
if __name__=='__main__':
    main()

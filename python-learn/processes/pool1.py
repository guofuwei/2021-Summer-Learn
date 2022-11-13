# pool1.py

from multiprocessing import Pool
import os
import time
import random

def worker(msg):
    t_start=time.perf_counter()
    print('%s开始执行，进程号为%d' %(msg,os.getpid()))
    time.sleep(random.random()*2)
    t_stop=time.perf_counter()
    print(msg,'执行完成，耗时%0.2fs' %(t_stop-t_start))

def main():
    print('-----start------')
    po=Pool(3)
    for i in range(0,10):
        po.apply_async(worker,(i,))
    po.close()
    po.join()
    print('-----end-----')

if __name__=='__main__':
    main()


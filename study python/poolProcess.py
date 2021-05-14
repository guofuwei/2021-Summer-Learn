from multiprocessing import Pool
import time,os


def fun(i):
    print("The %s(%s) process is running" %(i,os.getpid()))
    time.sleep(0.5)
    print("The %s(%s) process end" %(i,os.getpid()))


if __name__=='__main__':
    print("The parent process(%s) is running" %(os.getpid()))
    ci=Pool(4)
    for i in range(5):
        ci.apply_async(fun,args=(i,))
    print("Wait all the subprocess end...")
    ci.close()
    ci.join()
    print("All subprocesses done")

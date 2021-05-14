#!/usr/bin/env python3

# -*- coding: utf-8 -*-


from multiprocessing import managers,freeze_support
import random,time,queue
from multiprocessing.managers import BaseManager

task_queue=queue.Queue()
result_queue=queue.Queue()
def return_task_queue():
    global task_queue
    return task_queue

def return_result_queue():
    global result_queue
    return result_queue

class QueueManagers(BaseManager):
    pass




def test():
    QueueManagers.register('get_task_queue',callable=return_task_queue)
    QueueManagers.register('get_result_queue',callable=return_result_queue)

    manager=QueueManagers(address=('127.0.0.1',5000),authkey=b'abc')

    manager.start()

    task=manager.get_task_queue()
    result=manager.get_result_queue()

    for i in range(10):
        n = random.randint(0,10000)
        print('Put task %d ...'%n)
        task.put(n)

    print('Try get results...')
    for i in range(10):
        r=result.get(timeout=10)
        print('Result:%s'%r)

    manager.shutdown()
    print('master exit.')

if __name__=='__main__':
    freeze_support()
    print('Start!')
    test()

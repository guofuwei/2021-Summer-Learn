# copy_file.py

import os,time,random
from  multiprocessing import Pool
from multiprocessing import Manager
def copy_file(queue,old_folder_name,new_folder_name,file_name_one):
    time.sleep(random.random()/10)
    new_file=open(new_folder_name+'//'+file_name_one,'wb')
    old_file=open(old_folder_name+'//'+file_name_one,'rb')
#    print('---开始拷贝(%d)---' %file_name_one)
    while True:
        file_data=old_file.read(1024)
        if file_data:
            new_file.write(file_data)
        else:
            break

    new_file.close()
    old_file.close()

    queue.put(file_name_one)




def main():
    print('---文件夹拷贝开始---')
    # 1.获取用户要copy的文件夹名称
    old_folder_name=input('请输入要复制的文件夹名称:')

    # 2.创建一个新的文件夹
    if not os.path.exists('new_'+old_folder_name):
        os.mkdir('new_'+old_folder_name)

#    test_read=open(old_folder_name+'//'+'abc.py','rb')
#    test_data=test_read.read()
#    test_file=open('new'+old_folder_name+'/'+'test','wb')
#    test_file.write(test_data)
#    test_file.close() 

    # 3.获取文件夹里的所有待copy的文件名 listdir(path)
    file_name=os.listdir(old_folder_name)
#    print(file_name)
    # 4.复制原文件夹中的文件到新的文件夹中 copy_file
    po = Pool(10)
    queue=Manager().Queue()
    start=time.perf_counter()
    print('---文件正在拷贝请稍侯---')
    for i in range(len(file_name)):
        po.apply_async(copy_file,(queue,old_folder_name,'new_'+old_folder_name,file_name[i]))
    po.close()
#    po.join()
    # 打印复制文件进度
    rate=len(file_name)//50+1
    scale=len(file_name)//rate
    i=0
    while True:
        temp=queue.get()
        i+=1
        count=i//rate
        a = '*'*count
        b = '.'*(scale-count)
        c = (count/scale)*100
        dur=time.perf_counter()-start
        print('\r{:^3.0f}%[{}->{}]{:.2f}s'.format(c,a,b,dur),end='')
        if i==len(file_name):
            break

    print('\n---文件夹拷贝完成---')

if __name__=='__main__':
    main()
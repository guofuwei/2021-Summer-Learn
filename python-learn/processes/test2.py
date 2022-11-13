import multiprocessing

def download_from(q):
    data=[11,22,33,44]
    print('1',q)
    for temp in data:
        q.append(temp)
    print('2',q)
    print('数据已下载完成并成功写入队列!')

def analysis_data(q):
    print('3',q)

q=list()

def main():


    p1 = multiprocessing.Process(target=download_from,args=(q,))
    p2 = multiprocessing.Process(target=analysis_data,args=(q,))

    p1.start()
    p2.start()

if __name__=='__main__':
    main()

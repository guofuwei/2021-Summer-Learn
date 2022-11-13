import multiprocessing

def download_from(q):
    data=[11,22,33,44]
    for temp in data:
        q.put(temp)
    print('数据已下载完成并成功写入队列!')

def analysis_data(q):
    L=[]
    while not q.empty():
        L.append(q.get()+1)
    print(L)



def main():
    q=multiprocessing.Queue()

    p1 = multiprocessing.Process(target=download_from,args=(q,))
    p2 = multiprocessing.Process(target=analysis_data,args=(q,))

    p1.start()
    p2.start()

if __name__=='__main__':
    main()

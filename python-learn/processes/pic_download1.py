# pic_download1.py
import requests
import gevent

def downloader(img_name,img_url):
    req=requests.get(img_url)
    img_content=req.content
    with open(img_name,'wb') as f:
        f.write(img_content)
    
def main():
    gevent.joinall([
        gevent.spawn(downloader,'1.jpg','https://rpic.douyucdn.cn/live-cover/roomCover/2020/10/29/19d6fc5ae95c5d341758bc1bb6276911_big.png'),
        gevent.spawn(downloader,'2.jpg','https://rpic.douyucdn.cn/live-cover/appCovers/2021/06/03/9221175_20210603163231_small.jpg')
    ])

if __name__=='__main__':
    main()
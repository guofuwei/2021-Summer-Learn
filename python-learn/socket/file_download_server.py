# file_download_server.py

from socket import *
import time

def main():
    tcp_server=socket(AF_INET,SOCK_STREAM)
    tcp_server.bind(('',7788))
    tcp_server.listen(128)

    client_socket,client_addrs=tcp_server.accept()
    recv_data=client_socket.recv(1024).decode('utf-8')
    print('正在查找文件(%s)....' %recv_data)
    time.sleep(1)
    
    
    send_data=None
    try:
        f=open(recv_data,'rb')
        send_data=f.read()
        print('查找文件成功!')
        if send_data:
            time.sleep(0.5)
            client_socket.send(send_data)
            print('传输文件完成!')
    except:
        print('没有要下载的文件(%s)' %recv_data)
    

    client_socket.close()
    tcp_server.close()

if __name__=='__main__':
    main()
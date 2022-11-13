# flie_download.py
import sys
from socket import *

def main():
    tcp_client_socket=socket(AF_INET,SOCK_STREAM)
    server_ip=input('请输入要连接的服务器ip:')
    server_port=int(input('请输入要连接的服务器port:'))
    tcp_client_socket.connect((server_ip,server_port))  

    file_name=input('请输入要下载的文件名:')
    tcp_client_socket.send(file_name.encode('utf-8'))
    recv_data=tcp_client_socket.recv(1024*1024)
    if recv_data:
        with open('new'+file_name,'wb') as f:
            f.write(recv_data)
        print('文件已成功写入!')

    tcp_client_socket.close()

if __name__=='__main__':
    main()
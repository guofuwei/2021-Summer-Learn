# tcp_server2.py

from socket import *

def main():
    tcp_server_socket=socket(AF_INET,SOCK_STREAM)

    addrs=('',7788)
    tcp_server_socket.bind(addrs)
    tcp_server_socket.listen(128)

    while True:
        print('正在等待一个新的客户端.....')
        client_socket,client_addrs=tcp_server_socket.accept()
        print(client_addrs,end='')
        recv_data=client_socket.recv(1024)
        print(':%s' %recv_data.decode('utf-8'))
        client_socket.send('已收到'.encode('utf-8'))
        print('服务完毕!\n')

        client_socket.close()
    tcp_server_socket.close()

if __name__=='__main__':    
    main()


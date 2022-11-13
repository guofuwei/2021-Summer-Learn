# tcp_server3.py

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
        while True:
            recv_data=client_socket.recv(1024).decode('utf-8')
            if recv_data=='':
                break
            else:
                print('已收到:%s' %recv_data)
                client_socket.send('已收到消息'.encode('utf-8'))
        print('服务完毕!\n')

        client_socket.close()
    tcp_server_socket.close()

if __name__=='__main__':    
    main()


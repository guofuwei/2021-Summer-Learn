# tcp_client1.py

from socket import *

def main():
    tcp_client=socket(AF_INET,SOCK_STREAM)

    server_ip=input('请输入服务器的ip:')
    server_port=int(input('请输入服务器的port:'))

    tcp_client.connect((server_ip,server_port))

    send_data=input('请输入要发送的数据:')

    tcp_client.send(send_data.encode('utf-8'))

    recv_data=tcp_client.recv(1024)
    print('接收到的数据为:',recv_data.decode('utf-8'))

    tcp_client.close()

if __name__=='__main__':
    main()

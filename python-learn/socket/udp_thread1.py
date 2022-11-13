from socket import *
import threading

def send_msg(udp_socket,dest_addrs):
    while True:
        send_data=input('')
        udp_socket.sendto(send_data.encode('utf-8'),dest_addrs)

def recv_msg(udp_socket):
    while True:
        recv_msg=udp_socket.recvfrom(1024)
        print('%s:%s' %(recv_msg[1],recv_msg[0].decode('utf-8')))

def main():
    udp_socket=socket(AF_INET,SOCK_DGRAM)
    udp_socket.bind(('',7788))
#    dest_ip=input('请输入目标的ip:')
#    dest_port=int(input('请输入目标的port:'))
    dest_addrs=('192.168.153.1',8080)
    t1=threading.Thread(target=send_msg,args=(udp_socket,dest_addrs))
    t2=threading.Thread(target=recv_msg,args=(udp_socket,))
    t1.start()
    t2.start()


if __name__=='__main__':
    main()


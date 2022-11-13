import socket
udp_socket=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
udp_socket.bind(('',8080))
print('输入exit后退出程序')

while True:
    send_data=input('请输入要发送的数据:')
    if send_data=='exit':
        break
    udp_socket.sendto(send_data.encode('utf-8'),('192.168.153.128',8081))

udp_socket.close()

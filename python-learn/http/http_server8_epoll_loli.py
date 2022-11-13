# epoll利用共享内存和时间通知的方式提高了单线程非堵塞的效率
# epoll在win系统下不可用!!!
import socket
import re
import select

def service_client(client_socket,recv_data):
    request_lines=recv_data.splitlines()
    # 第一行格式为 GET /index.html HTTP/1.1
    # GET可能换为POST,PUT,DEL等
    # print(recv_data.decode('utf-8'))
    # 发送headers
    ret=re.match(r'[^/]+(/[^ ]*)',request_lines[0])
    if ret:
        file_name=ret.group(1)
        if file_name=='/':
            file_name='/index.html'
        print(file_name)
    try:
        f=open('./html'+file_name,'rb')
    except:
        response_body='---没有找到文件---'
        response_header='HTTP/1.1 404 NOT FOUND\r\n'+'Content-Type: text/html; charset=utf-8\r\n'+\
            'Content-Length:%d\r\n' %len(response_body) +'\r\n'
        response=response_header+response_body
        client_socket.send(response.encode('utf-8'))
    else:
        html_content=f.read().decode('utf-8')
        f.close()
        response_body=html_content
        response_header='HTTP/1.1 200 OK\r\n'+'Content-Type: text/html; charset=utf-8\r\n'+\
            'Content-Length:%d\r\n' %len(response_body) +'\r\n'
        response=response_header+response_body
        client_socket.send(response.encode('utf-8'))
    # 此时不需要调用close(),当浏览器请求完毕时会自动关闭


def main():
    http_server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

    # 保证服务器意外关闭时端口被保留占用无法再次开启
    http_server.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)

    http_server.bind(('',7788))
    http_server.listen(128)

    #创建一个epoll对象用于指向那块共享内存
    epl=select.epoll()
    epl.register(http_server.fileno(),select.EPOLLIN)
    # 创建一个字典将fd和套接字联系起来
    fd_event_dict=dict()

    while True:
        fd_event_list=epl.poll()  # 默认会堵塞在这里，以列表的形式返回fd,event 例如：[(fd1,event1),()]
        for fd,event in fd_event_list:
            if fd == http_server.fileno():
                client_socket,client_addrs=http_server.accept()
                epl.register(client_socket.fileno(),select.EPOLLIN)
                # 将新的套接字的fd和套接字联系起来
                fd_event_dict[client_socket.fileno()]=client_socket
            elif event==select.EPOLLIN:
                recv_data=fd_event_dict[fd].recv(1024).decode('utf-8')
                if recv_data:
                    service_client(fd_event_dict[fd],recv_data)
                else:
                    fd_event_dict[fd].close()
                    epl.unregister(fd)
                    del fd_event_dict[fd]

    http_server.close()

if __name__=='__main__':
    main()
            
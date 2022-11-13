import socket
import re

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
        response='HTTP/1.1 404 NOT FOUND\r\n'
        response+='Content-Type: text/html; charset=utf-8\r\n'
        response+='\r\n'
        response+='---没有找到文件---'
        client_socket.send(response.encode('utf-8'))
    else:
        html_content=f.read()
        f.close()
        response='HTTP/1.1 200 OK\r\n'
        response+='Content-Type: text/html; charset=utf-8\r\n'
        response+='\r\n'
        client_socket.send(response.encode('utf-8'))
        client_socket.send(html_content)
    client_socket.close()


def main():
    http_server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

    # 保证服务器意外关闭时端口被保留占用无法再次开启
    http_server.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)

    http_server.bind(('',7788))
    http_server.listen(128)

    # 设置监听套接字为非堵塞
    http_server.setblocking(False)
    # 设置客户套接字列表
    client_socket_list=list()

    # 重要 :非堵塞的核心代码如下:
    while True:
        try:
            client_socket,client_addrs=http_server.accept()
        except Exception as ret:
            # 下面可以打印错误信息
            # print(ret)
            pass
        else:
            client_socket.setblocking(False)
            client_socket_list.append(client_socket)
            
        # 开始循环客户套接字进行服务
        # 采用轮询的方式(for进行循环)
        for client in client_socket_list:
            try:
                recv_data=client.recv(1024).decode('utf-8')
            except Exception as ret:
                # print(ret)
                pass
            else:
                # 当recv_data为空，表明浏览器已经关闭，此时应从，关闭套接字并从列表中删除该套接字
                if recv_data:
                    service_client(client,recv_data)
                else:
                    client_socket_list.remove(client)
                    client.close()

    http_server.close()

if __name__=='__main__':
    main()
            
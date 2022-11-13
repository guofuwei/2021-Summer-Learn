import socket
import re

def service_client(client_socket):
    recv_data=client_socket.recv(1024).decode('utf-8')
    if recv_data:
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

    # 防止服务器意外关闭时端口被保留占用无法再次开启
    http_server.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)

    http_server.bind(('',7788))
    http_server.listen(128)

    while True:
        client_socket,client_addrs=http_server.accept()
        service_client(client_socket)
    http_server.close()

if __name__=='__main__':
    main()
            
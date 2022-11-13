import socket

def main():
    http_server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    # 保证服务器意外关闭时端口被保留占用无法再次开启
    http_server.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
    http_server.bind(('',7788))
    http_server.listen(128)
    html='''HTTP/1.1 200 OK\r\n\r\n<h1>hahah</h1>'''

    while True:
        client_socket,client_addrs=http_server.accept()
        recv_data=client_socket.recv(1024)
        print(recv_data.decode('utf-8'))
        client_socket.send(html.encode('utf-8'))
        client_socket.close()
    http_server.close()

if __name__=='__main__':
    main()
            
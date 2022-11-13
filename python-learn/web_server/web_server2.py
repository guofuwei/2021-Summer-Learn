# 实现动态资源的加载
import socket
import re
import multiprocessing
import mini_frame

class WSGIServer(object):
    def __init__(self):
        self.http_server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

        # 保证服务器意外关闭时端口被保留占用无法再次开启
        self.http_server.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)

        self.http_server.bind(('',7788))
        self.http_server.listen(128)

    def service_client(self,client_socket):
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

            if not file_name.endswith('.py'):
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
            else:
                header='HTTP/1.1 200 OK\r\n'
                header+='\r\n'
                # body=mini_frame.login()
                body=mini_frame.application(file_name)
                response=header+body
                client_socket.send(response.encode('utf-8'))
        client_socket.close()


    def run_forever(self):
        while True:
            client_socket,client_addrs=self.http_server.accept()
            p1=multiprocessing.Process(target=self.service_client,args=(client_socket,))
            p1.start()
            client_socket.close()
        self.http_server.close()

def main():
    wsgiserver=WSGIServer()
    wsgiserver.run_forever()

if __name__=='__main__':
    main()
            
# 实现接口和框架可变
import socket
import re
import multiprocessing
#import mini_frame
import sys

class WSGIServer(object):
    def __init__(self,port,app):
        self.http_server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

        # 保证服务器意外关闭时端口被保留占用无法再次开启
        self.http_server.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)

        self.http_server.bind(('',port))
        self.http_server.listen(128)
        self.application=app

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
                env=dict()
                env['PATH_INFO']=file_name
                body=self.application(env,self.set_response_header)

                header='HTTP/1.1 %s\r\n' %self.status
                for temp in self.headers:
                    header+='%s:%s\r\n' %(temp[0],temp[1])
                header+='\r\n'
                response=header+body
                client_socket.send(response.encode('utf-8'))
        client_socket.close()


    def set_response_header(self,status,headers):
        self.status=status
        self.headers=[('server','mini_web v1.0')]
        self.headers+=headers

    def run_forever(self):
        while True:
            client_socket,client_addrs=self.http_server.accept()
            p1=multiprocessing.Process(target=self.service_client,args=(client_socket,))
            p1.start()
            client_socket.close()
        self.http_server.close()

def main():
    if len(sys.argv)==3:
        try:
            port=int(sys.argv[1])
            frame_app_name=sys.argv[2]
        except Exception as ret:
            print('端口输入错误...')
            return
    else:
        print('请按照以下方式运行:')
        print('python xxx.py 7890 mini_frame:application')
        return 

    ret=re.match(r'([^:]+):(.*)',frame_app_name)
    if ret:
        frame_app_name=ret.group(1)
        app_name=ret.group(2)
    else:
        print('请按照以下方式运行:')
        print('python xxx.py 7890 mini_frame:application')
        return 

    sys.path.append('./web_server')
    frame=__import__(frame_app_name)
    app=getattr(frame,app_name)


    wsgiserver=WSGIServer(port,app)
    wsgiserver.run_forever()

if __name__=='__main__':
    main()
            
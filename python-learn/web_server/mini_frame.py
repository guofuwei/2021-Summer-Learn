from sre_constants import IN
from pymysql import *
import re
import logging

URL_FUNC_DICT=dict()

def route(url):
    def set_func(func):
        URL_FUNC_DICT[url]=func #  相当于URL_FUNC_DICT['/index.py']=index
        def call_func(*args,**kwargs):
            return func(*args,**kwargs)
        return call_func
    return set_func

@route(r"/index.html")
def index():
    with open('./html/index.html',encoding='utf-8') as f:
        content=f.read()
    conn=connect(host='localhost',port=3306,user='root',password='5017',database='test',charset='utf8')
    cs=conn.cursor()
    cs.execute("select id,name,citycode,yzcode from region limit 300;")
    region_infos=cs.fetchall()
    cs.close()
    conn.close()

    tr_template='''<body>
    <tr>
    <td>%s</td> 
    <td>%s</td>
    <td>%s</td>
    <td>%s</td>
    </tr>
    </body>
    '''
    for line_info in region_infos:
        content+=tr_template %(line_info[0],line_info[1],line_info[2],line_info[3])
    return content

@route(r"/center.html")
def center():
    return '<h1>这是个人中心页面</h1>'

# URL_FUNC_DICT={
#     "/index.py":index,
#     "/center.py":center
# }


def application(environ,start_response):
    start_response('200 OK',[('Content-Type','text/html;charset=utf-8')])
    
    file_name=environ['PATH_INFO']
    logging.basicConfig(level=logging.INFO,
        filename='./web_server/log.txt',filemode='a',
        format='%(asctime)s-%(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s'
    )
    logging.info('访问的是:%s' %file_name)
    # if file_name=='/index.html':
    #     return index()

    # elif file_name=='/center.py':
    #     return center()
    # else:
    #     return '<h1>Hello World!</h1>'
    try:
        # func=URL_FUNC_DICT[file_name]
        # return func()
        print(URL_FUNC_DICT.items())
        for url,func in URL_FUNC_DICT.items():
            ret=re.match(url,file_name)
            if ret:
                return func()
        else:
            logging.warning('没有对应的函数....')
            return '请求的url(%s)没有相应的函数' %file_name  
    except Exception as ret:
        return '产生了异常:%s' %ret
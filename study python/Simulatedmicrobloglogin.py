from urllib import request, parse

print('Login to weibo.cn...')
email = input('Email or PhonNumber: ')                    # 用户输入登录的邮箱名
passwd = input('Password: ')                # 用户输入登录的密码
login_data = parse.urlencode([              # 登录数据，用dict类型储存，parse.urlencode将dict转为url参数
    ('username', email),
    ('password', passwd),
    ('entry', 'mweibo'),
    ('client_id', ''),
    ('savestate', '1'),
    ('ec', ''),
    ('pagerefer', 'https://passport.weibo.cn/signin/welcome?entry=mweibo&r=http%3A%2F%2Fm.weibo.cn%2F')
])

req = request.Request('https://passport.weibo.cn/sso/login')  
req.add_header('Origin', 'https://passport.weibo.cn')
req.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36 Edg/90.0.818.51')
req.add_header('Referer', 'https://passport.weibo.cn/signin/login?entry=mweibo&res=wel&wm=3349&r=http%3A%2F%2Fm.weibo.cn%2F')

with request.urlopen(req, data=login_data.encode('utf-8')) as f:
    print('Status:', f.status, f.reason)             # 返回页面执行的状态
    for k, v in f.getheaders():                      # 得到HTTP相应的头和JSON数据
        print('%s: %s' % (k, v))
    print('Data:', f.read().decode('utf-8'))         # 得到页面信息

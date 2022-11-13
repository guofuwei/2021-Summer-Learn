
from urllib import request
url='https://www.douban.com/search?q=' 
key=request.quote('罪恶都市')					#由于字段含有中文，需要编码
url_all=url+key
header={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36 Edg/90.0.818.51'}
req=request.Request(url_all,headers=header)
with request.urlopen(req) as f:				#爬去网页
	data=f.read()

with open(r'C:\users\26254\desktop\dbsearch.html','wb') as fw:#写入文件
	fw.write(data)






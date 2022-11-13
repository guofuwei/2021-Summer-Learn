from pymysql import *

def main():
    conn=connect(host='localhost',port=3306,user='root',password='5017',database='test2',charset='utf8')
    
    cs1=conn.cursor()
    youin=input('请输入要查询的分类(1.性别 2.班级):')
    if youin=='1':
        count=cs1.execute('select gender as 性别,group_concat(name) as 姓名 from students group by gender;')
    elif youin=='2':
        count=cs1.execute('select cls_id as 班级,group_concat(name) as 姓名 from students group by cls_id;')
    else:
        print('输入错误')
        exit()
    print('查询到%d条数据:' %count)

    for i in range(count):
        result=cs1.fetchone()
        print(result)
    
    cs1.close()
    conn.close()

if __name__=='__main__':
    main()
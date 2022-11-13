from pymysql import *

class STU(object):
    def __init__(self):
        self.conn=connect(host='localhost',port=3306,user='root',password='5017',database='test2',charset='utf8')
        self.cs1=self.conn.cursor()

    def show(self,sql):
        self.cs1.execute(sql)
        for temp in self.cs1.fetchall():
            print(temp)
        
    def exit(self):
        self.cs1.close()
        self.conn.close()

    @staticmethod
    def print_meun():
        print('-------------------------')
        print('---请输入要查询的对象---')
        print('1:按性别查询')
        print('2:按班级查询')
        print('0:退出程序')
        return input('请输入要选择的功能:')

    def run(self):
        while True:
            num=self.print_meun()
            if num=='1':
                sql='select gender as 性别,group_concat(name) as 姓名 from students group by gender;'
                self.show(sql)
            elif num=='2':
                sql='select cls_id as 班级,group_concat(name) as 姓名 from students group by cls_id;'
                self.show(sql)
            elif num=='0':
                self.exit()
                break
            else:
                print('请重新输入!')
        print('程序已退出!')
            

def main():
    stu=STU()
    stu.run()

if __name__=='__main__':
    main()
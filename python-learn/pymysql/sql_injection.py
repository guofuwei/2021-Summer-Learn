from pymysql import *

class STU(object):
    def __init__(self):
        self.conn=connect(host='localhost',port=3306,user='root',password='5017',database='test2',charset='utf8')
        self.cs1=self.conn.cursor()

    def show(self,sql):
        self.cs1.execute(sql)
        for temp in self.cs1.fetchall():
            print(temp)

    def insert(self):
        in_stu=input('请输入要插入的学生姓名:')
        self.cs1.execute('''insert into students values(0,'%s',20,178,1,2,0)''' %in_stu)
        self.conn.commit()
    
    def find(self):
        find_stu=input('请输入要查询的学生姓名:')
        #以下方法存在sql注入的风险例如输入 ' or 1=1 or '1 可获取全部数据
        """print('---->%s<-----' %find_stu)
        self.cs1.execute('''select * from students where name='%s';''' %find_stu)
        print(self.cs1.fetchall())"""
        # 修改后
        sql='select * from students where name=%s'
        self.cs1.execute(sql,[find_stu])
        print(self.cs1.fetchall())
        
    def exit(self):
        self.cs1.close()
        self.conn.close()

    @staticmethod
    def print_meun():
        print('-------------------------')
        print('---请输入要查询的对象---')
        print('1:按性别查询')
        print('2:按班级查询')
        print('3:插入一个学生')
        print('4:查询某一个学生的信息')
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
            elif num=='3':
                self.insert()
            elif num=='4':
                self.find()
            else:
                print('请重新输入!')
        print('程序已退出!')
            

def main():
    stu=STU()
    stu.run()

if __name__=='__main__':
    main()
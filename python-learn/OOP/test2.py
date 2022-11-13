# 摆放家具
class House:
    def __init__(self,house_type,area):
        self.house_type=house_type
        self.area=area
        self.free_area=area
        self.item_list=[]

    def add_item(self,item):
        if item.area<=self.free_area:
            self.free_area-=item.area
            self.item_list.append(item.name)
        else:
            print('剩余空间不足,%s无法添加!\n' %item)

    def __str__(self):
        return ('户型:%s\n总面积:%.2f[剩余:%.2f]\n家具:%s'
        %(self.house_type,self.area,self.free_area,self.item_list))

class HouseItem:
    def __init__(self,name,area):
        self.name=name
        self.area=area

    def __str__(self):
        return '[%s] 占地 %s' %(self.name,self.area)

def main():
    bed=HouseItem('席梦思',40)
    chest=HouseItem('衣柜',2)
    table=HouseItem('餐桌',15)
    house=House('A型',150)
    house.add_item(bed)
    house.add_item(chest)
    house.add_item(table)
    print(house)

if __name__=='__main__':
    main()


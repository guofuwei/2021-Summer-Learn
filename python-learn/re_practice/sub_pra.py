# sub_pra.py

import re

def add(temp):
    strNum=temp.group()
    num=int(strNum)+1
    return str(num)

ret=re.sub(r'\d+',add,"python = 199")
print(ret)

# re.split(r',| ','25431b dhf,ydsf')
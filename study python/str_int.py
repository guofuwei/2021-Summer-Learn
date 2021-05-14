from functools import reduce
def str_int(s):
    DIGITS={'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'0':0}
    def fn(x,y):
        return x*10+y
    def char_num(i):
        return DIGITS[i]
    return reduce(fn,map(char_num,s))

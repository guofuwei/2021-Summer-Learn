from collections import OrderedDict

class LastUpdatedOrderedDict(OrderedDict):

    def __init__(self,capacity):
        super(LastUpdatedOrderedDict,self).__init__()
        self.capacity=capacity

    def __setitem__(self,key,value):
        containKey = 1 if key in self else 0
        if len(self)-containKey>=self.capacity:
            last=self.popitem(last=False)
            print('remove ',last)
        if containKey:
            del self[key]
            print('set',(key,value))
        else:
            print('add',(key,value))
        OrderedDict.__setitem__(self,key,value)
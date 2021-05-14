from contextlib import contextmanager

class Query(object):
    def __init__(self,name):
        self.name=name

    def query(self):
        print('Query info about %s...' %self.name)


@contextmanager
def creat_query(name):
    print('Begin')
    yield Query(name)
    print('End')

with creat_query('Bob') as q:
    q.query()
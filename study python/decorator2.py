import functools

def log(text):
    def decorator(func):
        @functools.wrap(func)
        def wrapper(*args,**kw):
            print('%s %s():'%(text,func._name_))
            return func(*args,**kw)
        return wrapper
    return decorator

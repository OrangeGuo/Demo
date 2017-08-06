import functools


def log(text):
    def decorator(fun):
        @functools.wraps(fun)
        def wrappers(*args, **kw):
            print('%s %s()' % (text, fun.__name__))
            return fun(*args, **kw)
        return wrappers
    return decorator


@log('begin')
def call():
    print('call is running')


call()


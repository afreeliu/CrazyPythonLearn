import functools as fun

'''
    该内容主要练习functools模块的函数的使用
'''


def test_decorator(f):
    # @fun.wraps(f)         # 1 ===============
    def wrapper(*args, **kwargs):
        print('这里是装饰了test函数后，优先在test函数前增加函数执行的内容')
        return f(*args, **kwargs)
    # return wrapper       # 1 ===============
    return fun.update_wrapper(wrapper, f)

@test_decorator
def atest(a):
    '''atest函数的说明信息'''
    print('这里执行test函数', a)


if __name__ == '__main__':
    print([e for e in dir(fun) if not e.startswith('_')])
    ['RLock', 'WRAPPER_ASSIGNMENTS', 'WRAPPER_UPDATES', 'cmp_to_key', 'get_cache_token', 'lru_cache', 'namedtuple',
     'partial', 'partialmethod', 'recursive_repr', 'reduce', 'singledispatch', 'total_ordering', 'update_wrapper',
     'wraps']
    atest(10)
    print(atest.__name__)
    print(atest.__doc__)




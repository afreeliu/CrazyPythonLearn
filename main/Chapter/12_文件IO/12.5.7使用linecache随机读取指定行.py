import linecache
import random

'''
    linecache 模块允许从 Python 源文件中随机读取指定行，并在内部使用优化存储。由于该模块主要被设计成读取Python源文件，因此它会使用UTF-8字符集
    来读取文件。实际上，使用linecache模块也可以读取其他文件，只要该文件使用了UTF-8字符集存储。
    linecache 模块常用函数如下：
    linecache.getline(filename, lineno, module_globals=None): 读取指定模块中指定文件的指定行。其中filename指定文件名，lineno指定行号
    linecache.clearcache(): 清空缓存
    linecache.checkcache(filename=None): 检查缓存是否有效，如果没有指定 filename 参数，则默认检查所有缓存的数据
'''

if __name__ == '__main__':
    # 读取 random 模块源文件的第3行
    print(linecache.getline(random.__file__, 3))

    # 读取本程序的第2行
    print(linecache.getline('12.5.7使用linecache随机读取指定行.py', 2))

    # 读取普通文件的第2行
    print(linecache.getline('ad', 2))

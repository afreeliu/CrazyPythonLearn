import sys
'''
    sys 模块代表了Python 解析器，主要用于获取和Python解析器相关信息
'''
def getSysModuleAllPatameter():
    '''
        获取sys模块中所有的属性变量和方法
    :return: void
    '''
    print([e for e in dir(sys) if not e.startswith('_')])


if __name__ == '__main__':
    print(getSysModuleAllPatameter.__doc__)
    getSysModuleAllPatameter()
    # 显示本地字节序的指示符
    print(sys.byteorder)
    # 显示与Python解析器有关的版权信息
    print(sys.copyright)
    # 显示Python解析器在磁盘上的存储路径
    print(sys.executable)
    # 显示在当前系统中保存文件所用的字符集
    print(sys.getfilesystemencoding())
    # 显示Python整数支持的最大值
    print(sys.maxsize)
    # 显示Python解析器所在的平台  macOS 显示的是 darwin(达尔文)
    print(sys.platform)
    # 显示当前Python解析器的版本信息
    print(sys.version)
    # 返回当前Python解析器的主版本
    # print(sys.winver)  该方法只在 windows 下可用

    # 返回当前 Python 解析器中线程切换的时间间隔。该属性可通过setswitchinterval()函数改变
    print(sys.getswitchinterval())
    sys.setswitchinterval(0.003)
    print(sys.getswitchinterval())

    # 返回当前Python解析器的实现
    print(sys.implementation)

    # 执行Python查找模块的路径列表。程序可通过修改该属性来动态增加Python加载模块的路径
    print(sys.path)
    # 返回 Python 解析器当前支持的递归深度。该属性可通过setrecursionlimit() 重新设置。
    print(sys.getrecursionlimit())




import fileinput

'''
    在前面的程序中，我们都采用程序主动关闭文件的方式。实际上，Python 提供了with语句来管理资源关闭。with语句如下
    with context_expression [as target(s)]:
        with 代码块
'''


class FKResource:
    def __init__(self, tag):
        self.tag = tag
        print('构造器，初始化资源：%s' % tag)

    # 定义 __enter__ 方法，他是在with代码块执行前执行的方法
    def __enter__(self):
        print('[__enter__ %s]: ' % self.tag)
        # 该返回值将作为 as 字句后的变量值
        return self # 可以返回任意类型的值

    # 定义 __exit__ 方法，他是在with代码块执行之后执行的方法
    def __exit__(self, exc_type, exc_val, exc_tb):
        print('[__exit__ %s]:' % self.tag)
        # exc_tb == exc_traceback 为 None 代表没有异常
        if exc_tb is None:
            print('没有异常时关闭资源')
        else:
            print('遇到异常时关闭资源')
            return False # 可以省略，默认返回None，也被看作是 False


if __name__ == '__main__':
    # 使用with 语句打开文件，该语句会负责关闭文件
    with open('ad', 'r', True, 'utf-8') as f:
        for line in f:
            print(line, end=' ')

    with fileinput.input(files=('UmPlatsFormGameManager.m')) as f:
        for line in f:
            print(line, end=';')

    with FKResource('孙悟空') as dr:
        print(dr.tag)
        print('[with 代码块] 没有异常')
    print('-------------------------------')
    with FKResource('白骨精'):
        print('[with 代码块] 异常之前的代码')
        raise Exception
        print('[with 代码块] ～～～～～～～～～ 异常之后的代码')





from pathlib import *
import fnmatch
'''
    fnmatch 模块可以支持类似于UNIX shell风格的文件名匹配
    fnmatch 匹配支持如下通识符：
    1、*：可匹配任意个任意字符
    2、？：可匹配一个任意字符
    3、[字符序列]：可匹配中括号里字符序列中的任意字符。该字符序列也支持中画线表示法。
        比如：[a-c]可代表a、b和c字符中任意一个
    4、[！字符序列]：可匹配不在中括号里字符序列中的任意字符。
    5、fnmatch.fnmatch(filename, pattern):判断制定文件名是否匹配制定pattern。
'''

if __name__ == '__main__':
    # 遍历当前目录下的所有文件和子目录
    for file in Path('./testDir').iterdir():
        # 访问所有以_test.py结尾的文件
        print(type(file))
        if fnmatch.fnmatch(file, '*_test.py'):
            print(file)
    # fnmatch.fnmatchcase(filename, pattern): 该函数与上一个函数的功能大致相同，只是该函数区分大小写
    # fnmatch.fileter(names, pattern): 该函数对names列表进行过滤，返回names列表中匹配pattern的文件名组成的子集合。
    names = ['a_test.py', 'btest.py', 'c_test.py']
    print(fnmatch.filter(names, 'a_*.py'))
    # fnmatch.translate(pattern): 该函数用于将一个UNIX shell风格的patter转换为正则表达式pattern
    print(fnmatch.translate('?.py'))
    print(fnmatch.translate('[ac].py'))
    print(fnmatch.translate('[a-c].py'))
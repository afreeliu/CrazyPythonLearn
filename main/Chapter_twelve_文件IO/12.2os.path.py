import os
import time
'''
    该内容主要练习的是 os.path 操作路径的内容
'''

if __name__ == '__main__':
    # 获取绝对路径
    print(os.path.abspath(''))

    # 获取共同前缀名
    print(os.path.commonprefix(['/usr/lib', '/usr/username/lib']))

    # 获取共同路径
    print(os.path.commonpath(['/usr/lib', '/usr/local/lib']))

    # 获取目录
    print(os.path.dirname('/usr/lib/liufei/liufei.txt'))

    # 判断指定目录是否存在
    print(os.path.exists('/usr/lib/liufei'))

    # 获取最近一次访问时间
    print(time.ctime(os.path.getatime('.')))

    # 获取最后一次修改时间
    print(time.ctime(os.path.getmtime('.')))

    # 获取创建时间
    print(time.ctime(os.path.getctime('12.2os.path.py')))

    # 获取文件大小
    print(os.path.getsize('12.2os.path.py'))

    # 判断是否为文件
    print(os.path.isfile('12.2os.path.py'))

    # 判断是否为目录
    print(os.path.isdir('.'))

    # 判断是否为同一个文件
    print(os.path.samefile('12.2os.path.py', './12.2os.path.py'))


    # a = 'abcdefgA'
    # b = 'gAAAAggbBCDDE'
    # print(len(set(a)))
    # print(len(set(b)))
    #
    # bb = set(b)
    # aa = set(a)
    # print()

    s = 'abcdefg'
    s = s.replace('a', '[a]')
    print(s.replace('a', '[a]'))
    # aa = list(s)
    # print(aa)
    # print(aa.pop())


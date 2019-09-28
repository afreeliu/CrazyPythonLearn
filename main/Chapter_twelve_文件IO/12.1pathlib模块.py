from pathlib import *
'''
    pathlib 模块提供了一组面向对象的类，这些类可代表各种操作系统上的路径，程序可通过这些类操作路径。
    
    PurePath 模块中主要是对路径的字符串操作，并不涉及到真实地操作文件文件夹
    
    Path 同样提供了两个子类：PosixPath 和 WindowsPath， 其中前者代表UNIX 风格的路径，后者代表Windows 风格的路径
    Path 对象包含了大量is_xxx()方法，用于判断该path对应的路径是否为xxx。Path 包含一个exists()方法，用于判断该Path对应的目录是否在。
    Path 还包含一个很常用的iterdir()方法，该方法可返回Path对应目录下的所有的子目录和文件。此外，
    Path 还包含一个glob()方法，用于获取Path对应目录及其子目录下匹配指定模式的所有文件。借助于glob()方法，可以非常方便地查找指定文件
'''


if __name__ == '__main__':

    # 创建PurePath，实际上使用PureWindowsPath或者PurePiosixPath
    pp = PurePath('test.py')
    print(type(pp))
    pp = PurePath('Crazy', 'some/path', 'info')
    print(pp)
    pp = PurePath(Path('Crazy'), Path('info'))
    print(pp)


    # 获取当前目录
    p = Path('.')
    print(p)
    # 遍历当前目录下的所有文件和子目录
    for e in p.iterdir():
        print(e)

    # 获取上一级目录
    p = Path('../')
    print(p)
    for e in p.glob('**/*.py'):
        print(e)
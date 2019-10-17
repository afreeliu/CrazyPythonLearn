from pathlib import *


if __name__ == '__main__':
    '''
            当使用open()函数打开文本文件时，程序使用的是哪种字符集呢？总是使用当前系统的字符集，比如Windows平台，
            open()函数总是使用GBK字符集。因此，上面程序读取的test.txt也必须使用GBK字符集保存；否则，程序就会
            出现 UnicodeDecodeError错误
            如果需要读取的文件所使用的字符集和当前操作系统的字符集不匹配，则有两种解决方式。
            1、使用二进制模式读取，然后用bytes的decode()方法恢复成字符串。
            2、利用open()函数来打开文件时通过encoding参数指定字符集。
    '''
    # 指定使用二进制模式读取文件内容
    imagefile = open('testfiledecoding.rtf', 'rb', True)
    # 直接读取全部文件内容，并调用bytes的decode()方法将字节内容恢复成字符串
    print(imagefile.read().decode('utf-8'))
    imagefile.close()

    # 指定使用utf-8字符集读取文件内容
    f = open('testfiledecoding.rtf', 'r', True, 'utf-8')
    while True:
        # 每次读取一个字符
        ch = f.read(1)
        # 如果没有读取到数据，则跳出循环
        if not ch: break
        print(ch)
    f.close()

    '''
        按行读取
        如果程序读取行，通常只能用文本方式来读取————只有文本才有行的概念，二进制文件没有所谓行的概念
    '''
    # readline([n]):读取一行内容。如果指定了参数n，则只读取此行内的n个字符。
    # readlines(): 读取文件内所有行。
    f_readline = open('testfiledecoding.rtf', 'r', True, 'utf-8')
    while True:
        # 每次读取一行
        line = f_readline.readline()
        # 如果没有读取到内容，就退出循环
        if not line: break
        # 输出内容
        print(line, end=' ')
    f_readline.close()
    print('---------------------------------')
    f_readlines = open('testfiledecoding.rtf', 'r', True, 'utf-8')
    # 使用readlines()读取所有行，返回所有组成的列表
    for l in f_readlines.readlines():
        print(l, end=' ')
    f_readlines.close()






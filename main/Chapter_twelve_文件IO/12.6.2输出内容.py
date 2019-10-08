
import os

'''
    文件对象提供的写文件的方法主要有两个。
    write(str 或者 bytes): 输出字符串或字节串。只有以二进制模式（b模式）打开的文件才能写入字节串。
    writelines(可迭代对象): 输出多个字符串或多个字节串。
'''


if __name__ == '__main__':
    f = open('12_6输出内容.txt', 'w+')
    # os.linesep 代表当前系统的换行符
    f.write('我爱Python' + os.linesep)
    f.writelines(('土门比神剑，' + os.linesep, '星源度以南。' + os.linesep, '是一夜城下，' + os.linesep, '纵思室友款。' + os.linesep))

    f1 = open('12_6输出内容为bytes.txt', 'wb+')
    # os.linesep 代表当前系统的换行符
    f1.write(('我爱Python' + os.linesep).encode('utf-8'))
    f1.writelines((('土门比神剑，' + os.linesep).encode('utf-8'), ('星源度以南。' + os.linesep).encode('utf-8'), ('是一夜城下，' + os.linesep).encode('utf-8'), ('纵思室友款。' + os.linesep).encode('utf-8')))
    f2 = open('12_6输出内容为bytes.txt', 'ab+')
    # os.linesep 代表当前系统的换行符
    f2.write(('我爱Python' + os.linesep).encode('utf-8'))
    f2.writelines((('土门比神剑，' + os.linesep).encode('utf-8'), ('星源度以南。' + os.linesep).encode('utf-8'),
                   ('是一夜城下，' + os.linesep).encode('utf-8'), ('纵思室友款。' + os.linesep).encode('utf-8')))
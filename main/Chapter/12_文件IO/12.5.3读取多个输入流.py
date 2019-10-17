import fileinput
'''
    fileinput 模块提供了如下函数可以把多个输入流合并在一起。
    fileinput.input(files=None, inplace=False, backup='', bufsize=0, mode='r', openhook=None):
        该函数中的files参数用于指定多个文件输入流。该函数返回一个FileInput对象。
    当程序中创建了FileInput对象之后，即可通过for-in循环来遍历文件的每一行。此外，fileinput还提供了如下全局函数来判断正在读取的文件信息
    fileinput.filename(): 返回正在读取的文件的文件名，
    fileinput.fileno(): 返回当前文件的文件描述符(file descriptor),该文件描述是一个整数
    fileinput.lineno(): 返回当前读取的行号
    fileinput.filelineno(): 返回当前读取的行在文件中的行号
    fileinput.isfirstline(): 返回当前读取的行在文件中是否为第一行
    fileinput.isstdin(): 返回最后一行是否从 sys.stdin 读取。程序可以使用"-"代表从 sys.stdin 读取
    fileinput.nextfile(): 关闭当前文件，开始读取下一个文件
    fileinput.close(): 关闭FileInput对象。
    
'''

if __name__ == '__main__':
    print('开始执行')
    # 一次读取多个文件
    for line in fileinput.input(files=('UmPlatsFormGameManager.h', 'UmPlatsFormGameManager.m')):
        # 输出文件名，以及当前行在当前文件中的行号
        print(fileinput.filename(), fileinput.filelineno(), line, end='\n')
    # 关闭文件流
    fileinput.close()
    print('执行完毕')
import sys
import re

'''
    管道的作用在于：将前一个命令的输出，当成下一个命令的输入。不管是UNIX系统（包括Mac OS X）还是Windows系统，都支持管道输入，
    管道输入的语法：cmd1 | cmd2 | cmd3
'''
if __name__ == '__main__':

    # 定义匹配E-mail的正则表达式
    mailPattern = r'([a-z0-9]*[-_]?[a-z0-9]+)*@([a-z0-9]*[-_]?[a-z0-9]+)+'\
        + '[\.][a-z]{2,3}([\.][a-z]{2})?'
    # 读取标准输入
    text = sys.stdin.read()
    # 使用正在表达式执行查找
    it = re.finditer(mailPattern, text, re.I)
    # 输出所有的电子邮件地址
    for e in it:
        print(str(e.span()) + "-->" + e.group())

    # 如果程序使用管道输入的方式，就可以把一个命令的输出当成 12.5.5管道输入.py 这个程序的输入
    # 例如使用如下命令: cat ad.txt | python 12.5.5管道输入.py



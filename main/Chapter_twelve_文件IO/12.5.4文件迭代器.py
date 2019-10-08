import sys


if __name__ == '__main__':

    f = open('UmPlatsFormGameManager.h', 'r', True, 'utf-8')
    # 使用for-in循环遍历问价对象
    for line in f:
        print(line, end=' ')
    f.close()

    # 将文件对象转换为list列表
    print(list(open('UmPlatsFormGameManager.m', 'r', True, 'utf-8')))

    # 使用 for-in 循环遍历标准输入
    for line in sys.stdin:
        print('用户输入：', line, end=' ')

    print('结束运行')


import os
'''
    os 模块代表了程序所在的操作系统，主要用于获取程序运行所在操作系统的相关信息
'''

if __name__ == '__main__':
    # __all__ 变量代表了该模块开放的公开借口
    print(os.__all__)
    # 返回导入依赖模块的的操作系统名称，通常可返回'posix'、'nt'、'java'等值其中之一
    print(os.name)
    # 返回在当前系统上所有环境变量组成的字典。
    print(os.environ)
    # 该函数对类路径(path-like)的文件名进行编码
    # print(os.fsencode(filename))
    # 该函数对类路径(path-like)的文件名进行编码
    # print(os.fsdecode(filename))
    # 这是一个类，代表一个类路径(path-like)对象
    print(os.PathLike)
    # 获取指定环境变量的值。
    # print(os.getenv('key', default=None))
    # 获取PYTHONPATH环境变量的值
    print(os.getenv('PYTHONPATH'))
    # 返回当前系统登录的用户的内容
    print(os.getlogin())
    print(os.getuid())
    print(os.getgroups())
    print(os.getgid())
    # 获取当前进程的ID
    print(os.getpid())
    # 获取当前进程的父进程ID
    print(os.getppid())
    # 该函数用于设置环境变量
    # print(os.putenv(key, value))
    # 返回当前系统的cpu的数量
    print(os.cpu_count())
    # 返回路径分隔符
    print(os.sep)
    # 返回当前系统上多条路径之间的分隔符。一般在windows系统上多条路径之间的分隔符
    # 是英文分号(;) ；在 UNIX 及 类UNIX 系统（如 Linux、Mac OS X）上多条路径
    # 之间的分隔符是英文冒号（:）
    print(os.pathsep)
    # 返回当前系统的换行符.一般在 Windows 系统上换行符是'\r\n';在UNIX系统上
    # 换行符是'\n'; 在 Mac OS X 系统上换行符是'\r'
    print(os.linesep)
    # 返回适合作为加密使用的、最多由N个字节组成的bytes对象。该函数通过操作系统
    # 特定的随机性来源返回随机字节，该随机字节通常是不可预测的，因此适用于绝大部分加密场景
    print(os.urandom(1))


    # os 模块下还包含各种进程管理函数，他们用于启动新程序、中止已有进程等。
    # os.abort(): 生成一个SIGABRT信号给当前进程。在UNIX系统上，默认行为是生成内核转储；
    #             在Windows系统上，进程立即返回退出代码3

    # os.execl(): 该函数还有一系列功能类的函数，比如:os.execle() os.execlp()等。
    #             这些函数都是适用参数列表arg0,arg1,...来执行path所代表的执行文件的

    # os.forkpty(): fork一个子进程
    # os.kill(pid=,sig=): 将sig信号发送到pid对应的进程，用于结束进程。
    # os.killpg(pgid=,sig=): 将sig信号发送到pgid对应的进程组
    # os.popen(cmd,mode='r',buffering=-1): 用于向cmd命令打开读写管道（当mode为r时为只读管道，当mode为rw时为读写管道，buffering缓冲
    #               参数与内置的open()函数相同的含义。该函数返回的文件对象用于读写字符串，而不是字节。
    # os.spawnl(mode,path,...): 该函数还有一系列功能类似的函数，比如os.spawnle(),os.spawnlp()等，这些函数都用于在新进程中执行新程序
    # os.startfile(path[,operation]): 对指定文件使用该文件关联的工具执行operation对应的操作。如果不指定operation操作，则默认执行
    #       打开（open）操作。operation参数必须是有效的命令行操作项目，比如open（打开），edit（编辑），print（打印）等。只有Windows可用
    # os.system(command): 运行操作系统上的指定命令。


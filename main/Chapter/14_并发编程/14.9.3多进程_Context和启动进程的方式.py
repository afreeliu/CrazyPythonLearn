import multiprocessing
import os

'''
    根据平台的支持， Python 支持三种启动进程的方式

    spawn: 父进程会启动一个全新的 Python 解释器进程。在这种方式下，子进程只能继承那些处理 run() 方法所必须的资源。典型的，那些不必要的文件
           描述器和 handle 都不会被继承。使用这种方式启动进程，其效率比使用 fork 或 forkserver 方式要低得多
           （ Windows 只支持使用 spawn 方式来启动进程，因此在 Windows 平台上默认使用这种方式来启动进程）

    fork: 父进程使用 os.fork() 来启动一个 Python 解释器进程。在这种方式下，子进程会继承父进程的所有资源，因此子进程基本等效于父进程。
          这种方式只在 UNIX 平台上有效， UNIX 平台默认使用这种方式来启动进程

    forkserver: 如果使用这种方式来启动进程，重将会启动一个服务器进程。在以后的时间内，当程序再次请求启动新进程时，父进程都会连接服务器进程，
                请求服务器进程来 fork 新进程。通过这种方式启动的进程不需要从父进程继承资源。这种方式只在 UNIX 平台上有效


    从上面结束可以看出，如果程序使用 UNIX 平台，Python 支持三种启动进程的方式；但如果使用 Windows 平台，则只能使用效率最低的 spawn 方式

    multiprocessing 模块提供了一个 set_start_method() 函数，该函数可用于设置启动进程的方式————必须将这行设置代码放在所有与多进程有关的
    代码之前。
'''


def foo(q):
    print('被启动的新进程：（%s)' % os.getpid())
    q.put('Python')

if __name__ == '__main__':
    # 设置使用 fork 方式启动进程
    multiprocessing.set_start_method('fork')
    q = multiprocessing.Queue()
    # 创建进程
    mp = multiprocessing.Process(target=foo, args=(q, ))
    # 启动进程
    mp.start()
    # 获取队列消息
    print(q.get())
    mp.join()

    '''
        上面程序中代码显式指定必须使用 fork 方式来启动进程，因此该程序只能在 UNIX 平台上运行。上面代码实际上就相当于使用 os.fork() 方法来创建启动新进程
    '''
    '''
        还有一种设置进程启动方式的方法，就是利用 get_context() 方法来获取 Context 对象，调用该方法是可传入 spawn、 fork 或 forkserver
        字符串。 Context 拥有和 multiprocessing 相同的 API， 因此程序可通过 Context 来创建并启动进程
    '''

    # 设置使用 fork 方式启动进程，并获取 Context 对象
    ctx = multiprocessing.get_context('fork')
    qq = ctx.Queue()
    # 创建进程
    mp2 = ctx.Process(target=foo, args=(qq,))
    # 启动进程
    mp2.start()
    print(qq.get())
    mp2.join()


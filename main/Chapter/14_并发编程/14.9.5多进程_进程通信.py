import multiprocessing
import os

'''
    Python 为进程通信提供了两种机制。

    Queue: 一个进程向 Queue 中放入数据，另一个进程从 Queue 总读取数据

    Pipe: Pipe 代表连接两个进程的管道。程序在调用 Pipe() 函数时会产生两个连接端，分别交给通信的两个进程，接下来进程既可从该连接端读取数据
          也可向该连接端写入数据。

'''

# 1 使用 Queue 实现进程通信
'''
    multiprocessing 模块下的 Queue 和 queue 模块下的 Queue 基本类似，它们都提供了 qsize()、empty()、full()、put()、 put_nowait()
    等方法。区别只是 multiprocessing 模块下的 Queue 为进程提供服务，而 queue 模块下的 Queue 为线程提供服务。
'''

# 2 使用 Pipe 实现进程通信
'''
    使用 Pipe 实现进程通信，程序会调用 multiprocessing.Pipe() 函数来创建一个管道，该函数会返回两个 PipeConnection 对象，代表管道的两个
    连接端（一个管道有两个连接端，分别用于连接通信的两个进程）。
    PipeConnection 对象包含如下常用方法
    send(obj): 发送一个 obj 给管道的另一端，另一端使用 recv() 方法接收。需要说明的是，该 obj 必须是可 picklable 的（Python 序列化机制）
               如果该对象序列化之后超过 32MB，则很可能会引发 ValueError 异常。
    recv(): 接收另一端通过 send() 方法发送过来的数据
    fileno(): 关于连接所使用的文件描述器
    close(): 关闭连接
    poll([timeout]): 返回连接中是否还有数据可以读取
    send_bytes(buffer[, offset[, size]]): 发送字节数据。如果没有指定 offset、size 参数，则默认发送 buffer 字节串的全部数据；如果指定
                                          了 offset 和 size 参数，则只发送 buffer 字节串中从 offset 开始、长度为 size 的字节数据
                                          通过该方法发送的数据，应该使用 recv_bytes() 或 recv_bytes_into 方法接收
    recv_bytes([maxlength]): 接收通过 send_bytes() 方法发送的数据，maxlength 指定最多接收的字节数。该方法返回接收到的字节数据
    recv_bytes_into(buffer[, offset]): 功能与 recv_bytes() 方法类似，只是该方法将接收到的数据放在 buffer 中
'''



# 第一种创建进程的方式
# def f(q):
#     print('(%s)进程开始放入数据。。。' % multiprocessing.current_process().pid)
#     q.put('Python')
#
# if __name__ == '__main__':
#     # 创建进程通信的 Queue
#     q = multiprocessing.Queue()
#     # 创建子进程
#     p = multiprocessing.Process(target=f, args=(q,))
#     # 启动子进程
#     p.start()
#
#     print('(%s)进程开始取出数据...' % multiprocessing.current_process().pid)
#     print(q.get())
#     p.join()


# 第二种创建进程通信的方式
def f(conn):
    print('(%s)进程开始发送数据...' % multiprocessing.current_process().pid)
    # 使用 conn 发送数据
    conn.send('Python')

if __name__ == '__main__':
    # 创建 Pipe，该函数返回两个 PipeConnection 对象
    parent_conn, child_conn = multiprocessing.Pipe()
    # 创建子进程
    p = multiprocessing.Process(target=f, args=(child_conn, ))
    # 启动子进程
    p.start()
    print('（%s）进程开始接收数据...' % multiprocessing.current_process().pid)
    # 通过 parent_conn 接收数据
    print(parent_conn.recv())
    p.join()
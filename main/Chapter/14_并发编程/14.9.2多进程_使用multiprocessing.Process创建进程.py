import multiprocessing
import os

'''
    虽然 os.fork() 方法可以启动多个进程，但这种方式显然不适合 Windows，而 Python 是跨平台的语言，所以 Python 绝不能仅仅局限于 Windows
    系统，因此 Python 也提供了其他方式在 Windows 下创建进程。
    Python 在 multiprocessing 模块下提供了 Process 来创建新进程。与 Thread 类似的是，使用 Process 创建新进程也有两种方式
    以指定函数作为 target，创建 Process 对象即可创建新进程。
    继承 Process 类，并重写它的 run() 方法来创建进程类，程序创建 Process 子类的实例作为进程。
    Process 类也有如下类似的方法和属性
    run(): 重写该方法可以实现进程的执行体。
    start(): 该方法用于启动进程。
    join([timeout]): 该方法类似于线程的 join() 方法，当前进程必须等待被 join 的进程执行完成才能向下执行。
    name: 该属性用于设置或访问进程的名字。
    is_alive(): 判断进程是否还活着。
    daemon: 该属性用于判断或设置进程的后台状态。
    pid: 返回进程的 ID。
    authkey: 返回进程的授权 key
    terminate(): 中断该进程
'''


# 第一种创建进程的方式：指定函数作为 target 来创建进程
# 定义一个普通的 action 函数，该函数准备作为进程执行体
def action(max):
    for i in range(max):
        print('(%s)子进程（父进程：（%s））：%d' % (os.getpid(), os.getppid(), i))


# 第二种创建进程的方式：继承 Process 类创建子进程
'''
    步骤如下：
    定义继承 Process 的子类，重写其 run() 方法准备作为进程执行体
    创建 Process 子类的实例
    调用 Process 子类的实例的 start() 方法来启动进程
'''
class my_mutilProcess(multiprocessing.Process):

    def __init__(self, max):
        self.max = max
        super().__init__()

    def run(self) -> None:
        for i in range(self.max):
            print('(%s)子进程（父进程：（%s））：%d' % (os.getpid(), os.getppid(), i))


if __name__ == '__main__':
    # # 下面是主程序
    # for i in range(100):
    #     print('(%s)主进程：%d' % (os.getpid(), i))
    #     if i == 20:
    #         # 创建第一个进程
    #         mp1 = multiprocessing.Process(target=action, args=(100,))
    #         mp1.start()
    #         # 创建第二个进程
    #         mp2 = multiprocessing.Process(target=action, args=(100,))
    #         mp2.start()
    #         mp2.join()
    # print('主进程执行完成!')
    # '''
    #     注意：因为 mp2 进程加入了 join() 方法，因此主进程必须等 mp2 进程完成后才能向下执行
    # '''

    # 验证第二种方式
    for i in range(100):
        print('(%s)主进程：%d' % (os.getpid(), i))
        if i == 20:
            mp1 = my_mutilProcess(100)
            mp1.start()
            mp2 = my_mutilProcess(100)
            mp2.start()
            mp2.join()
    print('主进程执行完成!')
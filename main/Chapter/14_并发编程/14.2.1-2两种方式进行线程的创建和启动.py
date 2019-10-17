
import threading


'''
    Python 提供了 _thread 和 threading 两个模块来支持多线程，其中 _thread 模块提供低级别的、原始的线程支持，以及一个简单的锁，正如它的
    名字锁暗示的，一般编程不建议使用 _thread 模块；而 threading 模块则提供了功能丰富的多线程支持。
    Python 主要通过两种方式来创建线程
    使用 threading 模块的 Thread 类的构造器创建线程
    继承 threading 模块的 Thread 类创建线程
    
    一、调用 Thread 类的构造器创建线程很简单，直接调用 threading.Thread 类的如下构造器创建线程。
    __init__(self, group=None, target=None, name=None, args=(), kwargs=None, *, daemon=None)
    
    group: 指定线程所属的线程组。目前该参数还没有实现，因此它只能是None
    target: 指定该线程要调用的目标方法
    args: 指定一个元组，以位置参数的形式为 target 指定的函数传入参数。元组的第一个元素传给 target 函数的第一个参数，以此类推
    kwargs: 指定一个字典，以关键字参数的形式为 target 指定的函数传入参数。
    daemon: 指定锁构建的线程是否为后台线程


    二、继承 Thread 类创建线程类
    通过继承 Thread 类来创建并启动线程的步骤如下。
    1 定义 Thread 类的子类，并重写该类的 run() 方法。 run()方法的方法体就代表了线程需要完成的任务，因此把 run() 方法成为线程执行体
    2 创建 Thread 子类的实例，即创建线程对象。
    3 调用线程对象的 start() 方法来启动线程
'''

# 通过继承 threading.Thread 类来创建线程类
class FKThread (threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.i = 0

    # 重写 run() 方法作为线程执行体
    def run(self) -> None:
        while self.i < 100:
            print(threading.current_thread().getName() + ' ' + str(self.i))
            self.i += 1



def action(max):
    for i in range(max):
        # 调用 threading 模块的 current_thread()函数获取当前线程
        # 调用线程对象的 getName() 方法获取当前线程的名字
        print(threading.current_thread().getName() + " " + str(i))

if __name__ == '__main__':
    # 第一个中创建线程的方式
    # for i in range(100):
    #     # 调用 threading 模块的 current_thread() 函数获取当前线程
    #     print(threading.current_thread().getName() + ' ' + str(i))
    #     if i == 20:
    #         # 创建并启动 t1 线程
    #         t1 = threading.Thread(target=action, args=(100,))
    #         t1.start()
    #         # 创建并启动 t2 线程
    #         t2 = threading.Thread(target=action, args=(100,))
    #         t2.start()
    # print('主线程执行完成')

    # 第二种创建线程的方法
    for i in range(100):
        print(threading.current_thread().getName() + ' ' + str(i))
        if i == 20:
            ft1 = FKThread()
            ft1.start()
            ft2 = FKThread()
            ft2.start()
    print('主线程执行完')




import threading
import time

'''
    当两个线程相互等待对方释放同步监视器时就会发生死锁。 Python 解释器没有监测，也没有采取措施来处理死锁情况，所以在进行多线程编程时应该采取
    措施避免出现死锁
    
    
    死锁是不应该在程序出现的，在编写程序的时候应该尽量避免出现死锁。下面几种常见的方式解决死锁问题：
    1 避免多次锁定：尽量避免统一线程对多个 Lock 进行锁定。
    2 具有相同的加锁顺序：如果多个线程需要对多个 Lock 进行锁定，则应该保证它们以相同的顺序请求加锁。
    3 使用定时锁：程序在调用 acquire() 方法加锁时可指定 timeout 参数，该参数指定超过 timeout 秒后会自动释放对 Lock 的锁定，这样就可以解开死锁
    4 死锁检测：死锁检测是一种依靠算法机制来实现的死锁预防机制，它主要是针对那些不可能实现按序加锁，也不能使用定时锁的场景的
    
'''


class A:
    def __init__(self):
        self.lock = threading.RLock()
        self.lock2 = threading.RLock()
    def foo(self, b):
        try:
            self.lock.acquire()
            print('当前线程名：' + threading.current_thread().name + '进入了 A 实例的 foo() 方法')
            time.sleep(0.2)
            print('当前线程名：' + threading.current_thread().name + '企图调用 B 实例的 last() 方法')
            b.last()
        finally:
            self.lock.release()
    def last(self):
        try:
            # self.lock.acquire()
            self.lock2.acquire()
            print('进入了 A 类的 last() 方法内部')
        finally:
            print('调用完毕 last')
            # self.lock.release()
            self.lock2.release()

class B:
    def __init__(self):
        self.lock = threading.RLock()
        self.lock2 = threading.RLock()
    def bar(self, a):
        try:
            self.lock.acquire()
            print('当前线程名：' + threading.current_thread().name + '进入了 B 实例的 bar() 方法')
            time.sleep(0.2)
            print('当前线程名：' + threading.current_thread().name + '企图调用 A 实例的 last() 方法')
            a.last()
        finally:
            self.lock.release()

    def last(self):
        try:
            # self.lock.acquire()
            self.lock2.acquire()
            print('进入 B 类的 last() 方法内部')
        finally:
            print('调用完毕 last')
            # self.lock.release()
            self.lock2.release()

a = A()
b = B()

def init():
    threading.current_thread().name = '主线程'
    # 调用 a 对象的 foo() 方法
    a.foo(b)
    print('进入了主线程之后')

def action():
    threading.current_thread().name = '副线程'
    # 调用 b 对象的 bar() 方法
    b.bar(a)
    print('进入副线程之后')

# 以 action 为 target 的启动新线程
threading.Thread(target=action).start()
# 调用 init() 函数
init()



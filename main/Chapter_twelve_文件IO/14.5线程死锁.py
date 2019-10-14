import threading
import time

'''
    当两个线程相互等待对方释放同步监视器时就会发生死锁。 Python 解释器没有监测，也没有采取措施来处理死锁情况，所以在进行多线程编程时应该采取
    措施避免出现死锁

'''


class A:
    def __init__(self):
        self.lock = threading.RLock

import threading
import time

'''
    Event 是一种非常简单的线程通信机制：一个线程发出一个 Event， 另一个线程可通过该 Event 被触发
    Event 本身管理一个内部标识，程序可以通过 Event 的 set() 方法将该标识设置为 True，也可以调用 clear() 方法将该标识设置为 False。
    程序可以调用 wait() 方法来阻塞当前线程，直到 Event 的内部标识设置为 True。
    
    is_set(): 该方法返回 Event 的内部标识是否为 True
    
    set(): 该方法将会把 Event 的内部标识设置为 True， 并唤醒所有处于等待状态的线程
    
    clear(): 该方法将 Event 的内部标识设置为 False，通常接下来会调用 wait() 方法来阻塞当前线程
    
    wait(timeout=None): 该方法会阻塞当前线程。 

'''


event = threading.Event()
def cal(name):
    # 等待事件，进入等待阻塞状态
    print('%s 启动' % threading.currentThread().getName())
    print('%s 准备开始计算状态' % name)
    event.wait() # 1⃣
    # 收到事件后进入运行状态
    print('%s 收到通知了。' % threading.currentThread().getName())
    print('%s 正式开始计算' % name)

# 创建并启动两个线程，它们都会在  1⃣  号代码处等待
threading.Thread(target=cal, args=('甲',)).start()
threading.Thread(target=cal, args=('乙',)).start()
time.sleep(2) # 2⃣
print('--------------------------')
# 发出事件
print('主线程发出事件')
event.set()
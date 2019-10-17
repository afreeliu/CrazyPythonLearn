
import threading



'''
    当线程被创建并启动以后，它既不是一启动就进入执行状态的，也不是一直处于执行状态的，在线程的生命周期中，他要经过新建（New）、就绪（Ready）、
    运行（Running）、阻塞（Blocked）、死亡（Dead）5 种状态。尤其是当线程启动以后，他不可能一直"霸占"着 CPU 独自运行，所以 CPU 需要在多个
    线程之间切换，于是线程状态也会多次在运行、就绪之间转换
    
    一 新建和就绪状态
    启动线程对象调用 start() 方法，而不是调用 run() 方法！永远不要调用线程对象的 run() 方法！调用 star() 方法来启动线程，系统会把该
    run() 方法当成线程执行体来处理；但如果直接调用线程对象的 run() 方法，则 run() 方法立即执行，而且在该方法返回之前其他线程无法并发执行
    ————也就是说，如果直接调用线程对象的 run() 方法，则系统把线程对象当成一个普通对象，而 run() 方法也是一个普通方法，而不是线程执行体
    
    二 运行和阻塞状态
    当发生如下情况时，线程将会进去阻塞状态：
    1 线程调用 sleep() 方法主动放弃其所占用的处理器资源。
    2 线程调用了一个阻塞式 I/O 方法，在该方法返回之前，该线程被阻塞
    3 线程试图获得一个锁对象，但该锁对象正被其他线程所持有
    4 线程在等待某个通知
    针对上面几种情况，当发生如下特定的情况时可以接触阻塞，让该线程重新进入就绪状态
    1 调用 sleep() 方法的线程经过了指定的时间
    2 线程调用的阻塞式 I/O 方法已经返回
    3 线程成功地获得了试图获取的锁对象
    4 线程正在等待某个通知时，其他线程发出了一个通知
    
    三 线程死亡
    线程会以以下三种方式结束，结束后就处于死亡状态。
     run() 方法或代表线程执行体的 target 函数执行完成，线程正常结束
     线程抛出一个未捕获的 Exception 或 Error。
    
    
'''

def action(max):
    for i in range(max):
        # 当直接调用 run() 方法时， Thread 的 name 属性返回的是该对象的名字而不是当前线程的名字
        # 使用 threading.current_thread().name 总是获取当前线程的名字
        print(threading.current_thread().name + " " + str(i))

if __name__ == '__main__':

    # for i in range(100):
    #     # 使用 threading.current_thread().name 总是获取当前线程的名字
    #     print(threading.current_thread().name + " " + str(i))
    #     if i == 20:
    #         # 直接调用线程对象的 run() 方法
    #         # 系统会把线程对象当成普通对象，把 run() 方法当成普通方法
    #         # 所以下面两行代码并不会启动两个线程，而是依次执行两个 run() 方法
    #         threading.Thread(target=action, args=(100,)).run()
    #         threading.Thread(target=action, args=(100,)).run()
    #         '''
    #             在调用线程对象的 run() 方法之后，该线程已经不再处于新建状态，不要再次调用线程对象的 start() 方法
    #         '''


    sd = threading.Thread(target=action, args=(100,))
    print(sd.is_alive(), sd.isAlive())
    for i in range(300):
        # 使用 threading.current_thread().name 总是获取当前线程的名字
        print(threading.current_thread().name + " " + str(i))
        if i == 20:
            # 启动线程
            sd.start()
            # 判断启动后线程的 is_alive() 值，输出 True
            print(sd.is_alive(), sd.isAlive())
        # 当线程处于新建、死亡两种状态时，is_alive() 为 False
        # 当 i > 20 时，该线程肯定已经启动过了，如果 sd.is_alive() 为 False 那么就处于死亡状态
        if i > 20 and not(sd.is_alive()):
            print('')
            # 试图再次启动该线程
            # sd.start()
            '''
                对已经死亡了的线程再次启动，那么会报 RuntimeError 的错误 
            '''
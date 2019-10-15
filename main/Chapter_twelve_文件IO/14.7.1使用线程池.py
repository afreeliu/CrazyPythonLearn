
from concurrent.futures import ThreadPoolExecutor
import threading
import time
'''
    线程池的基类是 concurrent.futures 模块中的 Executor， Executor 提供了两个子类，即 ThreadPoolExecutor 和 ProcessPoolExecutor，
    其中 ThreadPoolExecutor 用于创建线程池，而 ProcessPoolExecutor 用于创建进程池。

    如果使用线程池/进程池来管理类并发编程，那么只要将相应的 task 函数提交给线程池/进程池，剩下的事情就由线程池/进程池来搞定

    submit(fn, *args, *kwargs): 将 fn 函数提交给线程池。 *args 代表传给 fn 函数的参数， *kwargs 代表以关键字参数的形式为 fn 函数传入参数

    map(func, *iterables, timeout=None, chunksize=1): 该函数类似于全局函数 map(func, *iterables), 只是该函数将会启动多个线程，
                                                      以异步方式立即对 iterables 执行 map 处理

    shutdown(wait=True): 关闭线程池

    程序将 task 函数提交（submit）给线程池后，submit 方法会返回一个 Future 对象， Future 类主要用于获取线程任务函数的返回值。由于线程
    任务会在新线程中以异步方式执行，因此，线程执行的函数相当于一个"将来完成"的任务，所以 Python 使用 Future 来表示

    Future 提供的方法：
    cancel(): 取消该 Future 代表的线程任务。如果该任务正在执行，不可取消，则该方法返回 False； 否则，程序会取消该任务，并返回 True。

    cancelled(): 返回 Future 代表的线程任务是否被成功取消

    running(): 如果该 Future 代表的线程任务正在执行、不可被取消，该方法返回 True。

    done(): 如果该 Future 代表的线程任务被成功取消或执行完成，则该方法返回 True。

    result(timeout=None): 获取该 Future 代表的线程任务最后返回的结果。如果 Future 代表的线程任务还未完成，该方法将会只是当前线程，其中
                          timeout 参数指定最多阻塞多少秒

    exception(timeout=None): 获取该 Future 代表的线程任务所引发的异常。如果该任务成功完成，没有异常，则该方法返回 None。

    add_done_callback(fn): 为该 Future 代表的线程任务注册一个"回调函数"，当该任务成功完成时，程序会自动触发该 fn 函数。

    在用完一个线程池后，应该调用该线程池的 shutdown()，该方法将启动线程池的关闭序列。调用 shutdown() 方法后的线程池不再接收新任务，但会
    将以前所有的已提交的任务执行完成。当线程池中的所有任务都执行完成后，该线程池中的所有线程都会死亡

    使用线程池执行任务的步骤如下：
    1 调用 ThreadPoolExecutor 类的构造器创建一个线程池
    2 定义一个普通函数作为线程任务
    3 调用 ThreadPoolExecutor 对象的 submit() 方法来提交线程任务
    4 当不想提交任何任务时，调用 ThreadPoolExecutor 对象的 shutdown() 方法来关闭线程池。
'''



# 定义一个准备作为线程任务的函数
def action(max):
    my_sum = 0
    for i in range(max):
        print(threading.currentThread().getName() + ' ' + str(i))
        my_sum += i
    return my_sum

# # 创建一个包含两个线程的线程池
# pool = ThreadPoolExecutor(max_workers = 2)
# # 向线程池中提交一个任务，50 会作为 action() 函数的参数
# future1 = pool.submit(action, 50)
# # 向线程池中提交一个任务，100 会作为 action() 函数的参数
# future2 = pool.submit(action, 100)
# # 判断 future1 代表的任务是否结束
# print(future1.done())
# time.sleep(3)
# # 判断 future2 代表的任务是否结束
# print(future2.done())
# # 判断 future1 代表的任务返回的结果
# print(future1.result())
# # 判断 future2 代表的任务返回的结果
# print(future2.result())
# # 关闭线程池
# pool.shutdown()

'''
    获取执行结果
    
    前面程序调用了 Future 的 result() 方法来获取线程任务的返回值，但该方法会阻塞当前主线程，只有等到线程任务完成后，result()方法的阻塞才会被解除
    
    如果程序不希望直接调用 result() 方法阻塞线程，则可通过 Future 的 add_done_callback() 方法来添加回调函数，该回调函数形如 fn(future)
    当线程任务完成后，程序会自动触发该回调函数，并将对应的 Future 对象作为参数传给该回调函数。

'''

# 创建一个包含两个线程的线程池  使用 with 方法创建的线程池可以避免手动关闭线程池
with ThreadPoolExecutor(max_workers=2) as pool:
    # 向线程池中提交一个任务，50 会作为 action() 函数的参数
    future1 = pool.submit(action, 50)
    # 向线程池中提交一个任务，100 会作为 action() 函数的参数
    future2 = pool.submit(action, 100)
    def get_result(future):
        print(future.result)
    # 为 future1 添加线程完成的回调函数
    future1.add_done_callback(get_result)
    # 为 future2 添加线程完成的回调函数
    future2.add_done_callback(get_result)
    print('------------------------------')

'''
    使用 map() 方法来启动 3 个线程（该程序的线程池包含 4 个线程，如果继续使用只包含 2 个线程的线程池，此时将有一个任务处于等待状态，必须
    等其中一个任务完成、线程空闲出来才会获得执行的机会），map() 方法的返回值将会收集每个线程任务的返回结果。
    运行下面的程序，统一可以看到 3 个线程并发执行的结果，最后通过 results 可以看到 3 个线程任务的返回结果
    通过下面程序可以看出，使用 map() 方法来启动线程，并收集线程的执行结果，不仅具有代码简单的优点，而且虽然程序会以并发方式来执行 action()
    函数，但最后收集的 action() 函数的执行结果，依然与传入参数的结果保持一致。也就是说，下面 results 的第一个元素是 action(50) 的结果，
    第二个元素是 action(100) 的结果，第三个元素是 action(150) 的结果
'''
with ThreadPoolExecutor(max_workers=4) as pool:
    # 使用线程执行 map 计算
    # 后面的元组有 3 个元素，因此程序启动了 3 个线程来执行 action 函数
    results = pool.map(action, (50, 100, 150))
    print('++++++++++++++++++++++++++++++++')
    for r in results:
        print(r)
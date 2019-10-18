
from urllib.request import *
import urllib.parse
import threading
'''
    在 urllib.request 子模块下包含了一个非常实用的 urllib.request.openurl(url, data=None) 方法，该方法用于打开 url 指定的资源，
    并从中读取数据。根据请求 url 的不同，该方法的返回值会发生动态改变。如果 url 是一个 HTTP 地址，那么该方法返回一个 http.client.HTTPResponse
    对象。

'''

# 打开 URL 对应的资源
# result = urlopen('http://www.crazyit.org/index.php')
# # 按字节读取数据
# data = result.read(326)
# # 将字节数据恢复成字符串
# print(data.decode('utf-8'))
#
# # 用 context manager 来管理打开的 URL 资源
# with urlopen('http://www.crazyit.org/index.php') as f:
#     print(f)
#     # 按字节读取数据
#     data = f.read(326)
#     print(data.decode('utf-8'))

'''
    在使用 urlopen() 函数时，可以通过 data 属性向被请求的 URL 发送数据
'''

# # 向 https://localhost/cgi-bin/test.cgi 发送请求数据  因为没有配置服务器，因此无法请求
# with urlopen(url='https://localhost:8888/test/test', data='测试数据'.encode('utf-8')) as f:
#     # 读取服务器的全部响应数据
#     print(f.read())

# # 如果使用 urlopen() 函数向服务器页面发送 GET 请求参数，则无须使用 data 属性，直接把请求参数附加在 URL 之后即可。
# params = urllib.parse.urlencode({'name': 'fkit', 'password': '123456'})
# # 将请求参数添加到 URL 后面
# url = 'https://localhost:8888/test/get.jsp?%s' % params
# print(url)
# with urlopen(url=url) as f:
#     print(f.read().decode('utf-8'))

# POST 请求
# params = urllib.parse.urlencode({'username': '13824472562', 'password': '1111111'})
# with urlopen(url = 'http://47.92.93.177:5577/api/authorizations',
#              data=params.encode('utf-8')) as f:
#     print(f.read())

'''
    实际上，使用 data 属性不仅可以发送 POST 请求，还可以发送 PUT、PATCH、DELETE 等请求，此时需要使用 urllib.request.Request 来构建
    请求参数。程序使用 urlopen() 函数打开远程资源时，第一个 url 参数既可以是 URL 字符串，也可以使用 urllib.request.Request 对象。
    urllib.request.Request 对象的构造器如下：
    urllib.request.Request(url, data=None, headers={}, origin_req_host=None, unverifiable=False, method=None): 从构造器可以
    看出，使用 Request 可以通过 method 指定请求方法，也可以通过 data 指定请求参数，还可以通过 headers 指定请求头。
'''

# PUT 请求
# params = 'put 请求数据'.encode('utf-8')
# # 创建 Request 对象，设置使用 PUT 请求方式
# req = Request(url='http://localhost:8888/test/put', data=params, method='PUT')
# with urlopen(req) as f:
#     print(f.status)
#     print(f.read().decode('utf-8'))

# # 使用 Reuqest 对象，为请求添加头部信息 headers
# req = Request('http://localhost:8888/test/header.jsp')
# req.add_header('Referer', 'http://www.crazyit.org/')
# with urlopen(req) as f:
#     print(f.status)
#     print(f.read().decode('utf-8'))


class DownUtil:
    def __init__(self, path, target_file, thread_num):
        # 定义下载资源的路径
        self.path = path
        # 定义需要多少个资源下载资源
        self.thread_num = thread_num
        # 指定所下载的文件保存的位置
        self.target_file = target_file
        #初始化 threads 数组
        self.threads = []

    def download(self):
        # 创建 Request 对象
        req = Request(url=self.path, method='GET')
        # 添加头请求
        req.add_header('Accept', '*/*')
        req.add_header('Charset', 'UTF-8')
        req.add_header('Connection', 'Keep-Alive')
        # 打开要下载的资源
        f = urlopen(req)
        print(f.headers)
        # 获取要下载的文件大小
        self.file_size = int(dict(f.headers).get('Content-Length', 0))
        f.close
        # 计算每个线程要下载的资源大小
        current_part_size = self.file_size // self.thread_num + 1
        for i in range(self.thread_num):
            # 计算每个线程下载的开始位置
            start_pos = i * current_part_size
            # 每个线程都使用一个以 wb 模式打开的文件进行下载
            t = open(self.target_file, 'wb')
            # 定位该线程下载的位置
            t.seek(start_pos, 0)
            # 创建下载线程
            td = DownThread(self.path, start_pos, current_part_size, t)
            self.threads.append(td)
            # 启动下载线程
            td.start()
    # 获取完成的百分比
    def get_complete_rate(self):
        # 统计多个线程已经下载的资源总大小
        sum_size = 0
        for i in range(self.thread_num):
            sum_size += self.threads[i].length
        # 返回已经完成的百分比
        return sum_size / self.file_size

class DownThread(threading.Thread):
    def __init__(self, path, start_pos, current_part_size, current_part):
        super().__init__()
        self.path = path
        # 当前线程的下载位置
        self.start_pos = start_pos
        # 定义当前线程负责下载的文件大小
        self.current_part_size = current_part_size
        # 当前线程需要下载的文件块
        self.current_part = current_part
        # 定义该线程已下载的字节数
        self.length = 0
    def run(self):
        # 创建 Request 对象
        req = Request(url=self.path, method='GET')
        # 添加请求头
        req.add_header('Accept', '*/*')
        req.add_header('Charset', 'UTF-8')
        req.add_header('Connection', 'Keep-Alive')
        # 打开要下载的资源
        f = urlopen(req)
        # 跳过 self.start_pos 个字节，表明该线程只下载自己负责的那部分内容
        for i in range(self.start_pos):
            f.read(1)
        # 读取网络数据，并写入本地文件中
        while self.length < self.current_part_size:
            data = f.read(1024)
            if data is None or len(data) <= 0:
                break
            self.current_part.write(data)
            # 累计该线程下载的资源总大小
            self.length += len(data)
        self.current_part.close()
        f.close

'''
     上面程序中定义了 DownThread 线程类，该线程类负责读取从 start_pos 开始、长度为 current_past_size 的所有字节数据，并写入本地文件
     对象中。DownThread 线程类的 run() 方法就是一个简单的输入/输出实现。
     程序中 DownUtils 类的 download() 方法负责按如下步骤来实现多线程下载
     1 使用 urlopen() 方法打开远程资源
     2 获取指定的 URL 对象所指向资源的大小（通过 Content-Length 响应头获取）。
     3 计算每个线程应该下载网络资源的哪个部分（从哪个字节开始， 到哪个字节结束）
     4 依次创建并启动多个线程来下载网络资源的指定部分
'''
aurl = 'https://image.baidu.com/search/down?tn=download&amp;word=download&amp;ie=utf8&amp;fr=detail&amp;url=https%3A%2F%2Ftimgsa.baidu.com%2Ftimg%3Fimage%26quality%3D80%26size%3Db9999_10000%26sec%3D1571371702433%26di%3Dfeac361f470c5bca2363a816e9068a02%26imgtype%3D0%26src%3Dhttp%253A%252F%252Fb-ssl.duitang.com%252Fuploads%252Fitem%252F201208%252F30%252F20120830031623_Ys2LQ.jpeg&amp;thumburl=https%3A%2F%2Fss1.bdstatic.com%2F70cFuXSh_Q1YnxGkpoWK1HF6hhy%2Fit%2Fu%3D1491992360%2C2030420109%26fm%3D26%26gp%3D0.jpg'
du = DownUtil(aurl, 'a.png', 3)
du.download()
def show_process():
    print('已完成 %.2f' % du.get_complete_rate())
    global t
    if du.get_complete_rate() < 1:
        # 通过定时器启动 0.1s 之后执行 show_process 函数
        t = threading.Timer(0.1, show_process)
        t.start()
t = threading.Timer(0.1, show_process)
t.start()








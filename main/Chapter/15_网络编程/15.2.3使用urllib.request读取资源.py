
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

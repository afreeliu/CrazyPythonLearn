
from urllib.request import *
import http.cookiejar, urllib.parse
import json

'''
    有时候，用户可能需要访问 Web 应用中的被保护的页面，如果使用浏览器则十分简单，通过系统提供的登录页面登录系统，浏览器会负责维护与服务器
    之间的 session，如果用户登录的用户名，密码符合要求，就可以访问被保护资源了

    如果使用 urllib.request 模块来访问被保护页面，则同样需要维护与服务器之间的 session，此时就需要借助于 cookie 管理器来实现。

    如果程序直接使用 urlopen() 发送请求，冰球并为管理与服务器之间的 session，那么服务器就无法识别两次请求是否是同一个客服端发出的。
    为了有效地管理 session，程序可引入 http.cookiejar 模块。

    此外程序还需要使用 OpenerDirector 对象来管理发送请求。
    为了使用 urllib.request 模块通过 cookie 来管理 session，可按如下步骤进行操作

    1 创建 http.cookiejar.CookieJar 对象或其子类的对象。
    2 以 CookieJar 对象为参数，创建 urllib.request.HTTPCookieProcessor 对象，该对象负责调用 CookieJar 来管理 cookie
    3 以 HTTPCookieProcessor 对象为参数，调用 urllib.request.build_opener() 函数创建 OpenerDirector 对象。
    4 使用 OpenerDirector 对象来发送请求，该对象将会通过 HTTPCookieProcessor 调用 CookieJar 来管理 cookie。

'''


# 以指定文件创建 CookieJar 对象，该对象可以把 cookie 信息保存在文件中
cookie_jar = http.cookiejar.MozillaCookieJar('a.txt')
# 创建 HTTPCookieProcessor 对象
cookie_processor = HTTPCookieProcessor(cookie_jar)
# 创建 OpenerDirector 对象
opener = build_opener(cookie_processor)

# 定义模拟 Chrome 浏览器的 User-Agent
user_agent = r'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36'
# 定义请求头
headers = {'User-Agent': user_agent, 'Connection': 'keep-alive'}

# ----------------------- 下面代码发送登录的 POST 请求
# params = {'username': '13824472562', 'password': '123456'}
params = {'phone': '13824472562', 'type': '1'}
postdata = urllib.parse.urlencode(params).encode()

# 创建向登录页面发送 POST 请求的 Reuest
# request = Request('http://47.92.93.177:5566/#/login', data=postdata, headers=headers)
request = Request('http://101.132.113.84:11002/userua/verify/login', data=postdata)
# 使用 OpenerDirector 发送 POST 请求
response = opener.open(request)
result = response.read().decode('utf-8')

d = json.loads(result)
print(d, type(d))

# 将 cookie 信息写入文件中
cookie_jar.save(ignore_discard=True, ignore_expires=True)


# ---------------------- 下面代码发送访问被保护资源的 GET 请求
# 创建向被保护页面发送 GET 请求的 Request
# request = Request('http://47.92.93.177:5566/#/login', headers=headers)
# response = opener.open(request)
# print(response.read().decode)

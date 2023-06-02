#导包
import requests

#设置url ,发送http get请求，获取响应结果
resp = requests.get("http://www.baidu.com")
#打印响应状态码
print("响应状态码=",resp.status_code)
#打印请求的URL
print("URL=",resp.url)
#打印头部编码
print("头部编码=",resp.encoding)
#打印头信息
print("头信息=",resp.headers)
#打印cookie
print("cookie=",resp.cookies)
#打印text 文本
print("文本数据=",resp.text)


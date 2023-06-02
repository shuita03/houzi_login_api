#导包
import  requests
#设置url 发送get请求，获取响应结果
#方式1
# url = "http://tpshop-test.itheima.net/Home/Goods/search.html?q=iPhone"
#方式2

url = "http://tpshop-test.itheima.net/Home/Goods/search.html"
params = {"q":"iPhone"}
resp = requests.get(url=url,params=params)

#打印响应状态码和响应结果
print("响应状态码=",resp.status_code)
print("resp=",resp.text)
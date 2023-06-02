#导包
import requests

#设置url,header,body,发送post请求，获取响应结果
url = "http://hmshop-test.itheima.net/Home/user/login.html"
header =  {"Content-Type":"application/x-www-form-urlencoded"}
body = {"username":"15100001111","password":"123456","verify_code":"8888"}

resp = requests.post(url=url,headers=header,data=body)

#打印一下响应状态码和响应结果
print("响应状态码=",resp.status_code)
print("resp=",resp.json())
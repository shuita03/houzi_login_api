#导包
import requests
#设置url,header,body ,发送http post请求，并且获取响应结果
login_url = "http://ihrm-test.itheima.net/api/sys/login"
login_header={"Content-Type": "application/json"}
login_data = {"mobile": "13800000002","password": "123456"}

resp = requests.post(url=login_url,headers=login_header,json=login_data)

#打印响应状态码 和响应结果
print("响应状态码=",resp.status_code)
print("resp=",resp.json())
import requests

login_url = ' https://www.72crm.com/api-11/login'
login_header = {'Content-Type': 'application/json;charset=UTF-8'}
login_data = {"username": "15122571345", "password": "123456qwer"}

# 发送接口请求
resp_login = requests.post(url=login_url, headers=login_header, json=login_data)

# 获取响应结果，并打印
print('响应码', resp_login.status_code)
print('返回文本', resp_login.json())

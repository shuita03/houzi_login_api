# 导包
import requests

# 设置url,header,body,发送put请求，获取响应结果
modify_emp_url = "http://ihrm-test.itheima.net/api/sys/user/1536600321130823680"
modify_emp_header = {"Content-Type": "application/json", "Authorization": "2cdaa011-3cde-46e1-a315-9da1ef1a6183"}
modify_emp_body = {"username": "齐天大圣"}

resp = requests.put(url=modify_emp_url, headers=modify_emp_header, json=modify_emp_body)

# 打印一下响应状态码和响应结果
print("响应状态码=", resp.status_code)
print("resp=", resp.json())

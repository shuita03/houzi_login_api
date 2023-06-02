# 导包
import requests

# 设置url,header, 发送delete请求，获取响应结果
del_emp_url = "http://ihrm-test.itheima.net/api/sys/user/1536600321130823680"
del_emp_header = {"Authorization": "2cdaa011-3cde-46e1-a315-9da1ef1a6183"}

resp = requests.delete(url=del_emp_url, headers=del_emp_header)

# 打印一下响应状态码和响应结果
print("响应状态码=", resp.status_code)
print("resp=", resp.json())

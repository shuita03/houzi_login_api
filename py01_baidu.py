# 导包
import requests

# 设置url（准备测试数据）
url = "http://www.baidu.com"
# 发送http get 请求，获取响应结果
resp = requests.get(url=url)

# 打印响应状态码和响应结果
print("响应状态码=", resp.status_code)
print("resp=", resp.text)



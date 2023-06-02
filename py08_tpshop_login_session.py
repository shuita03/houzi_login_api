# 导包
import requests

# 1. 创建一个Session 实例
session = requests.session()

# 2. 使用Session实例， 发送获取验证码请求
verify_code_url = "http://hmshop-test.itheima.net/index.php?m=Home&c=User&a=verify"
session.get(url=verify_code_url)

# 3. 使用同一个Session实例，调用post方法，发送登录请求
login_url = "http://hmshop-test.itheima.net/index.php?m=Home&c=User&a=do_login"
login_header = {"Content-Type": "application/x-www-form-urlencoded"}
login_data = {"username": "13012345678", "password": "123456", "verify_code": "8888"}
login_resp = session.post(url=login_url, headers=login_header, data=login_data)
print("login_resp=", login_resp.json())

# 4. 使用同一个Session实例，调用get方法，发送 查看我的订单请求
order_url = "http://hmshop-test.itheima.net/home/Order/order_list.html"
order_resp = session.get(url=order_url)
print("响应状态码=", order_resp.status_code)
print("order_resp", order_resp.text)

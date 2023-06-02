# 导包
import requests
'''
# 1. 调用get方法，发送 获取验证码的请求，获取响应结果
verify_code_url = 'http://hmshop-test.itheima.net/index.php?m=Home&c=User&a=verify&r=0.11480194278988143'
verify_code_resp = requests.get(url=verify_code_url)
# print("verify_code_resp=",verify_code_resp.text)

# 2. 从获取验证码的响应结果中，提取cookie
my_cookie = verify_code_resp.cookies
print("my_cookie=", my_cookie)
'''

# 3. 调用post方法，访问登录的接口，设置url, header, body, 注意并且携带cookie
login_url = "http://hmshop-test.itheima.net/index.php?m=Home&c=User&a=do_login"
login_header = {"Content-Type": "application/x-www-form-urlencoded"}
login_data = {"username": "13012345678", "password": "123456", "verify_code": "8888"}
login_resp = requests.post(url=login_url, headers=login_header, data=login_data)
print("login_resp=", login_resp.json())
'''
# 4. 调用get方法，发送 查看我的订单请求，注意设置携带cookie,打印结果
order_url = "http://hmshop-test.itheima.net/home/Order/order_list.html"
order_resp = requests.get(url=order_url, cookies=my_cookie)
print("响应状态码=", order_resp.status_code)
print("order_resp=", order_resp.text)
'''
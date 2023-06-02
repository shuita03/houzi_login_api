import requests

session = requests.session()
# 发送验证码请求
session.get('http://hmshop-test.itheima.net/index.php?m=Home&c=User&a=verify&type=user_reg&r=0.9956046474144453')

# 准备登录接口数据
login_url = 'http://hmshop-test.itheima.net/Home/User/reg.html'
login_header = {"Content-Type": "application/x-www-form-urlencoded"}
login_date = {'auth_code': 'TPSHOP', 'scene': '1', 'username': '15122224446', 'verify_code': '8888',
              'password': '709b586f9562ec782d8ae4ab618a4e51',
              'password2': '709b586f9562ec782d8ae4ab618a4e51', 'invite': '15166667777'}
resp_reg = session.post(url=login_url, headers=login_header, data=login_date)

print(resp_reg.status_code, resp_reg.json())

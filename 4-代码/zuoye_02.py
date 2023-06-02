import requests
import pytest


class TestTphopRegist(object):

    def test01_regist_success(self):
        # 创建session实例
        session = requests.session()
        # 发送验证码请求
        resp_v = session.get(
            'http://hmshop-test.itheima.net/index.php?m=Home&c=User&a=verify&type=user_reg&r=0.9956046474144453')

        # 准备登录接口数据
        login_url = 'http://hmshop-test.itheima.net/Home/User/reg.html'
        login_header = {"Content-Type": "application/x-www-form-urlencoded"}
        login_date = {'auth_code': 'TPSHOP', 'scene': '1', 'username': '15122241416', 'verify_code': '8888',
                      'password': '709b586f9562ec782d8ae4ab618a4e51',
                      'password2': '709b586f9562ec782d8ae4ab618a4e51', 'invite': '15166667777'}
        # 获取响应数据
        resp_reg = session.post(url=login_url, headers=login_header, data=login_date)

        # 获取响应数据，并打印
        print(resp_reg.status_code, resp_reg.json())

        # 断言
        assert resp_reg.status_code == 200
        assert resp_reg.json().get('status') == 1

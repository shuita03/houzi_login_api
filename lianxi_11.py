# 导包
import requests


# 创建类
class TestTPshopLogin(object):

    # 登录成功
    def test01_login_success(self):
        # 创建session实例
        session = requests.session()

        # 发送验证码
        reps_v = session.get('http://hmshop-test.itheima.net/index.php?m=Home&c=User&a=verify&r=0.340723506418364')

        # 准备登录接口的数据
        login_url = 'http://hmshop-test.itheima.net/index.php?m=Home&c=User&a=do_login&t=0.24157012570235192'
        login_header = {'Content-Type': 'application/x-www-form-urlencoded'}
        login_data = {'username': '15122223333', 'password': '123456qwer', 'verify_code': '8888'}

        # 发送接口请求
        resp_login = session.post(url=login_url, headers=login_header, data=login_data)

        # 获取响应数据并打印
        print(resp_login.status_code, resp_login.json())

        # 断言
        assert resp_login.status_code == 200
        assert resp_login.json().get('status') == 1
        assert resp_login.json().get("msg") == '登陆成功'

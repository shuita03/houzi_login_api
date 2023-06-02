# 导包
import requests

class HouziLogin(object):

    @classmethod
    def houzi_api(cls,json_data):
        url = 'https://www.72crm.com/api-11/login'
        header = {"Content-Type": "application/json"}
        response = requests.post(url=url,headers=header,json=json_data)
        return response
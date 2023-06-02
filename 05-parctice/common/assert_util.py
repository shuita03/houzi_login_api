
class AssretUtil(object):

    @classmethod
    def assert_login(cls,msg,response):
        assert msg == response.json().get('msg')

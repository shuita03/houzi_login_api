from api import houzi_login_api
import config
from parameterized import parameterized
from common import rade_json_util
from common import assert_util


class TestHouziLogin(object):
    data_path = config.BASE_DIR + '/data/houzi_login_data.json'

    @parameterized.expand(rade_json_util.ReadJsonUtil.rade_data(data_path))
    def test_houzi(cls, body, msg):
        response = houzi_login_api.HouziLogin.houzi_api(body)
        # res =houzi_login_api.HouziLogin.houzi_api(body)
        assert_util.AssretUtil.assert_login(msg, response)

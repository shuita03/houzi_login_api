import json
import config


class ReadJsonUtil:

    @classmethod
    def rade_data(cls, file_path):
        # 2. 打开json文件
        with open(file_path, "r", encoding="utf8") as f:
            # 3. 读取json文件。
            json_data = json.load(f)

        # 定义空列表
        list_data = []

        # 遍历json_data中的数据
        for item in json_data:
            # 提取遍历的value值，并转化为元祖
            temp = tuple(item.values())
            list_data.append(temp)
        return list_data


if __name__ == '__main__':
    file_path = config.BASE_DIR + '/data/houzi_login_data.json'
    result = ReadJsonUtil.rade_data(file_path)
    print(file_path)
    print(result)

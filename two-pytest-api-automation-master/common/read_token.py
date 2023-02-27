import os
import configparser


def read_token(token):
    conf_file = os.path.abspath(os.path.dirname(os.path.dirname(__file__)) + r"/configs/token.ini")  # 保存文件路径
    config = configparser.ConfigParser()
    config.read(conf_file, encoding='utf-8')
    xin_token = config.get("token", "{}".format(token))
    return xin_token

if __name__ == '__main__':
    read_token('zhangsan_token')
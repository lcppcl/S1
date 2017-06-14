import sys
import os
path = os.path.abspath(__file__)   #打印当前文件的绝对路径
current_dir = os.path.dirname(path)  #打印当前文件所在的目录
current_dir2 = os.path.dirname(current_dir)
base_dir = os.path.dirname(current_dir2)  #打印当前文件所在的目录
sys.path.append(base_dir)  #添加到环境变量中

from config import settings
def db_auth(configs):
    if configs.DATABASE['user'] == 'root' \
    and configs.DATABASE['password'] == '123':
        print('登录成功')
        return True
    else:
        print('登录失败')


def select(table, column):
    if db_auth(settings):
        if table == 'user':
            user_info = {
                '001': ['lcp', 22, 'engineer'],
                '002': ['lcp2', 22, 'engineer3'],
                '003': ['lcp3', 22, 'engineer3']
            }
            return user_info
    else:
        pass
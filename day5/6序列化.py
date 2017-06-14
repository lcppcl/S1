#序列化   支持所有的数据类型
import pickle
f = open('user.txt', 'wb')
def login():
    print('oh')
info = {
    'lcp': '123',
    'jack': '456',
    'func': login
}
#f.write(pickle.dumps(info))  #dumps对应loads
pickle.dump(info, f)  #dump对应load
f.close()


import json
f = open('user2.txt', 'w')

info = {
    'lcp': '123',
    'jack': '456'
}
f.write(json.dumps(info))
f.close()
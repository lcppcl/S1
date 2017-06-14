#反序列化
import pickle
def login():
    print('om')
f = open('user.txt', 'rb')

#data_from_atm = pickle.loads(f.read())
data_from_atm2 = pickle.load(f)
data_from_atm2['func']()
print(data_from_atm2)
f.close()


import json
f = open('user2.txt', 'r')
data_from_atm = json.loads(f.read())
print(data_from_atm)
f.close()
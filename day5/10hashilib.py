import hashlib

#只要输入值一样，加密的结果都是一样
m = hashlib.md5()  #声明用什么类型加密
m.update(b"Hello")  #加密一段字符串
m.update(b"It's me")
print(m.digest())  #以二进制输出
print(m.hexdigest())  #以16进制输出
m.update(b"It's been a long time since last time we ...")

print(m.digest())  # 2进制格式hash
print(len(m.hexdigest()))  # 16进制格式hash
'''
def digest(self, *args, **kwargs): # real signature unknown
    """ Return the digest value as a string of binary data. """
    pass

def hexdigest(self, *args, **kwargs): # real signature unknown
    """ Return the digest value as a string of hexadecimal digits. """
    pass

'''
import hashlib

# ######## md5 ########

hash = hashlib.md5()
hash.update(b'admin')
print(hash.hexdigest())

# ######## sha1 ########

hash = hashlib.sha1()
hash.update(b'admin')
print(hash.hexdigest())

# ######## sha256 ########

hash = hashlib.sha256()
hash.update(b'admin')
print(hash.hexdigest())

# ######## sha384 ########

hash = hashlib.sha384()
hash.update(b'admin')
print(hash.hexdigest())

# ######## sha512 ########

hash = hashlib.sha512()
hash.update(b'admin')
print(hash.hexdigest())


import hmac
h = hmac.new(b'LCP', b'OK')
print(h.hexdigest())
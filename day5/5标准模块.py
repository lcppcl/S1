'''
from model.XXX.XXX  import as SSS  #去别名
from model.XXX.XXX  import *  #导入所有模块，不推介使用
'''

import time
import datetime
'''
print(time.clock())  #返回处理器时间
print(time.process_time())  #返回处理器时间
print(time.time())  #返回当前系统的时间戳，时间为1秒
print(time.ctime())  #返回当前系统时间，默认格式  Wed Jun  7 23:56:05 2017
print(time.ctime(123212))  #将指定时间转化成系统默认格式
print(time.gmtime())  #time.struct_time(tm_year=2017, tm_mon=6, tm_mday=7, tm_hour=15, tm_min=58, tm_sec=33, tm_wday=2, tm_yday=158, tm_isdst=0)
print(time.mktime(time.localtime()))
print(time.strftime("%Y-%m %d %H %M %S"))  #将当前时间转换成指定格式输出
print(time.strptime("2013-01-23",'%Y-%m-%d'))  #将指定时间转换成time.struct_time格式time.struct_time(tm_year=2013, tm_mon=1, tm_mday=23, tm_hour=0, tm_min=0, tm_sec=0, tm_wday=2, tm_yday=23, tm_isdst=-1)
'''


import random
print(random.random())  #random.random()随机小数
print(random.randint(1,20))
print(random.randrange(1,20))
#生成随机验证码
checkcode = ''
for i in range(4):
    current = random.randrange(0, 4)
    if current != i:
        temp = chr(random.randint(65, 90))  #chr()把数字对应ascll码对应的字母取出来
    else:
        temp = random.randint(0, 9)
    checkcode += str(temp)
print(checkcode)



import os
'''
os.getcwd()  #获取当前工作目录
os.chdir('dirname')  #改变当前脚本工作目录
os.curdir  #返回当前目录 ('.')
os.pardir  #获取当前目录的父目录（'..'）
os.makedirs('dirname1/dirname2')  #递归生成多个目录
os.removedirs('dirname')  #若目录为空，则删除，并递归到上一级目录，若不为空，则删除其中所有文件
os.mkdir('dirname')  #生成单级目录
os.rmdir('dirname')  #删除单极空目录，若目录不为空则无法删除
os.listdir('dirname')  #列出指定目录下的所有文件和子目录，包含隐藏文件
os.remove()  #删除一个文件
os.rename('oldname', 'newname')  #重命名文件
os.stat('path/filename')  #获取文件/目录信息
os.sep  #输出操作系统特定的路径分隔符  win：\\, linux: /
os.linesep  #输出当前平台使用的行终止符 win：\t\n, linux:\n
os.pathsep  #输出用于分割文件的路径的字符串
os.name  #输出字符串指示当前使用平台。win->'nt'; Linux->'posix'
os.system("bash command")  #运行shell命令，直接显示
os.environ    #获取系统环境变量
os.path.abspath(path)  #返回path规范化的绝对路径
os.path.split(path)  #将path分割成目录和文件名二元组返回
os.path.dirname(path)  #返回path的目录。其实就是os.path.split(path)的第一个元素
os.path.basename(path)  #返回path最后的文件名。如何path以／或\结尾，那么就会返回空值。即os.path.split(path)的第二个元素
os.path.exists(path)  #如果path存在，返回True；如果path不存在，返回False
os.path.isabs(path)  #如果path是绝对路径，返回True
os.path.isfile(path)  #如果path是一个存在的文件，返回True。否则返回False
os.path.isdir(path)  #如果path是一个存在的目录，则返回True。否则返回False
os.path.join(path1[, path2[, ...]])  #将多个路径组合后返回，第一个绝对路径之前的参数将被忽略
os.path.getatime(path)  #返回path所指向的文件或者目录的最后存取时间
os.path.getmtime(path)  #返回path所指向的文件或者目录的最后修改时间
'''


import sys
'''
sys.argv          # 命令行参数List，第一个元素是程序本身路径
sys.exit(n)       # 退出程序，正常退出时exit(0)
sys.version       # 获取Python解释程序的版本信息
sys.maxint        # 最大的Int值
sys.path          # 返回模块的搜索路径，初始化时使用PYTHONPATH环境变量的值
sys.platform      # 返回操作系统平台名称
sys.stdout.write('please:')
val = sys.stdin.readline()[:-1]  #去掉最后一个回车符
'''

#进度条
for i in range(10):
    sys.stdout.write('#')
    sys.stdout.flush()
    time.sleep(0.3)


import shutil  #可以拷贝文件，压缩文件
'''
shutil.copyfile( src, dst)	 #从源src复制到dst中去。当然前提是目标地址是具备可写权限。抛出的异常信息为IOException. 如果当前的dst已存在的话就会被覆盖掉
shutil.copymode( src, dst)	 #只是会复制其权限其他的东西是不会被复制的
shutil.copystat( src, dst)	 #复制权限、最后访问时间、最后修改时间
shutil.copy( src, dst)   	 #复制一个文件到一个文件或一个目录
shutil.copy2( src, dst) 	 #在copy上的基础上再复制文件最后访问时间与修改时间也复制过来了，类似于cp –p的东西
shutil.copy2( src, dst) 	 #如果两个位置的文件系统是一样的话相当于是rename操作，只是改名；如果是不在相同的文件系统的话就是做move操作
shutil.copytree(olddir,newdir,True/Flase)	  #把olddir拷贝一份newdir，如果第3个参数是True，则复制目录时将保持文件夹下的符号连接，如果第3个参数是False，则将在复制的目录下生成物理副本来替代符号连接
'''


import shelve
d = shelve.open('shelve_test')

class Test(object):
    def __init__(self, n):
        self.n = n

t = Test(123)
t2 = Test(456)
name = ['lcp', 'rain', 'test']
d['test'] = name  #持久化列表
d['t1'] = t  #持久化类
d['t2'] = t2
d.close()
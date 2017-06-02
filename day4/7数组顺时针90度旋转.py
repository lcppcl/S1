a = [i for i in range(10)]
print(a)
print("---------------")
a = [[col for col in range(4)] for row in range(4)]  #二维列表
print(a)
for i in a:
    print(i)
print("---------------")


"""
[0, 1, 2, 3]
[0, 1, 2, 3]
[0, 1, 2, 3]
[0, 1, 2, 3]
------------
[0, 0, 0, 0]
[1, 1, 1, 1]
[2, 2, 2, 2]
[3, 3, 3, 3]
"""

data = [[col for col in range(4)] for row in range(4)]  #二维列表
print(data)
# 通过enumerate函数找到array的行索引和行数
for r_index, row in enumerate(data):
    for c_index in range(r_index, len(row)):
        tmp = data[c_index][r_index]
        data[c_index][r_index] = data[r_index][c_index]
        data[r_index][c_index] = tmp

    for r in data:
        print(r)

# 初始化一个4*4的数组
array2 = [[col for col in range(4)] for row in range(4)]
for i in range(len(array2)):
    array_new = [array2[i][i] for row in range(4)]
    print(array_new)
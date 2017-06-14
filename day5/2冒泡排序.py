'''
对无序的数组进行排序
'''
data = [10, 99, 4, 32, 54, 656, ]
for j in range(1, len(data)):
    for i in range(len(data)-j):
        if data[i] > data[i + 1]:
            temp = data[i + 1]
            data[i + 1] = data[i]
            data[i] = temp
print(data)
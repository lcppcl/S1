data = list(range(1, 600, 3))
print(data)


def binary_search(data_source, find_n):
    mid = len(data_source) // 2
    if len(data_source) >= 1:
        if data_source[mid] > find_n:  #data in left
            print("data in  left [%s]" % data_source[:mid])
            binary_search(data_source[:mid], find_n)
        elif data_source[mid] < find_n:
            print("data in  right [%s]" % data_source[mid:])
            binary_search(data_source[mid:], find_n)
        else:
            print("find_n in data_source %s" % data_source[mid])
    else:
        print('cannot find')


if __name__ == '__main__':
    data = list(range(1, 600))
    binary_search(data, 432)
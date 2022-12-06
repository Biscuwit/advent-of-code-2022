with open('data.txt') as file:
    data = file.read()


def find_marker(data: str, n_distinct):
    index = 0
    while True:
        cur = set(data[index:index+n_distinct])
        if len(cur) < n_distinct:
            index += 1
            continue
        else:
            return index + n_distinct


if __name__ == '__main__':
    start_marker = find_marker(data, 4)
    msg_marker = find_marker(data, 14)
    print(start_marker)
    print(msg_marker)



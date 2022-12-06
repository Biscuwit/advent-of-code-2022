with open('data.txt', 'r') as fh:
    f = fh.read()

cals_list = [list(map(int, stock_list.split('\n'))) for stock_list in f.split('\n\n')]
cal_sums = [sum(cals) for cals in cals_list]

if __name__ == '__main__':

    # part one
    print(max(cal_sums))

    # part two
    print(sum(sorted(cal_sums, reverse=True)[:3]))

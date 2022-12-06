with open('data.txt') as file:
    pairs = file.read().splitlines()

with open('data.txt') as f:
    p2 = [l.strip() for l in f.readlines()]
    assert pairs == p2

fully = 0
overlap = 0
for line in pairs:
    secs = [sec.split('-') for sec in line.split(',')]
    s1_start = int(secs[0][0])
    s1_end = int(secs[0][1])
    s2_start = int(secs[1][0])
    s2_end = int(secs[1][1])
    if s1_start <= s2_start and s1_end >= s2_end:
        fully += 1
    elif s2_start <= s1_start and s2_end >= s1_end:
        fully += 1

    if (s1_start <= s2_start <= s1_end) or (s1_start <= s2_end <= s1_end):
        overlap += 1
    elif (s2_start <= s1_start <= s2_end) or (s2_start <= s1_end <= s2_end):
        overlap += 1

if __name__ == '__main__':
    print(fully)
    print(overlap)

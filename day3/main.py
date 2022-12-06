import string

with open('data.txt') as file:
    backpacks = file.read().splitlines()

prio = {s: i+1 for i, s in enumerate(list(string.ascii_letters))}
groups = [backpacks[x:x+3] for x in range(0, len(backpacks), 3)]
sum1 = 0
sum2 = 0


for bp in backpacks:
    comp1 = set(bp[:int(len(bp)/2)])
    comp2 = set(bp[int(len(bp)/2):])
    conflict = comp1.intersection(comp2).pop()
    sum1 += prio[conflict]

for group in groups:
    sets = [set(g) for g in group]
    conflict = set.intersection(*sets).pop()
    sum2 += prio[conflict]

if __name__ == '__main__':
    print(sum1)
    print(sum2)

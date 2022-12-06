with open('data.txt') as fh:
    f = fh.read().splitlines()
win = 6
draw = 3
loss = 0
rock = 1
paper = 2
scissor = 3
mapping1 = {
    'A': {
        'X': rock + draw,
        'Y': paper + win,
        'Z': scissor + loss,
    },
    'B': {
        'X': rock + loss,
        'Y': paper + draw,
        'Z': scissor + win,
    },
    'C': {
        'X': rock + win,
        'Y': paper + loss,
        'Z': scissor + draw,
    }
}
mapping2 = {
    'A': {
        'X': scissor + loss,
        'Y': rock + draw,
        'Z': paper + win,
    },
    'B': {
        'X': rock + loss,
        'Y': paper + draw,
        'Z': scissor + win,
    },
    'C': {
        'X': paper + loss,
        'Y': scissor + draw,
        'Z': rock + win,
    }
}

scores1 = [mapping1[line.split(' ')[0]][line.split(' ')[1]] for line in f]
scores2 = [mapping2[line.split(' ')[0]][line.split(' ')[1]] for line in f]


if __name__ == '__main__':
    print(sum(scores1))
    print(sum(scores2))

import itertools
import re

with open('data.txt') as file:
    data = file.read().split('\n\n')
    stacks = data[0]
    moves = data[1]


class Move:
    def __init__(self, n_boxes, from_stack, to_stack):
        self.n = int(n_boxes)
        self.f = int(from_stack) - 1
        self.t = int(to_stack) - 1

    def __repr__(self):
        return f'move {self.n} items from stack {self.f} to stack {self.t}'


def parse_moves(m):
    moves = [_parse_move_row(row) for row in m.splitlines()]
    return moves


def _parse_move_row(row: str):
    n, f, t = tuple(re.findall(r'\d+', row))
    return Move(n_boxes=n, from_stack=f, to_stack=t)


def parse_stacks(s):
    parsed_stack = [_parse_stacks_row(row) for row in s.splitlines()][:-1]
    transposed_stacks = list(map(list, itertools.zip_longest(*parsed_stack, fillvalue=None)))
    filtered_stacks = [list(filter(str.strip, filter(None, row))) for row in transposed_stacks]
    return filtered_stacks


def _parse_stacks_row(row: str):
    return [letter for letter in row[1:-1:4]]


def move(s: list[list[str]], m: Move):
    to_move = s[m.f][:m.n]
    to_move.reverse()
    del s[m.f][:m.n]
    s[m.t] = to_move + s[m.t]


def move_multiple(s: list[list[str]], m: Move):
    to_move = s[m.f][:m.n]
    del s[m.f][:m.n]
    s[m.t] = to_move + s[m.t]


if __name__ == '__main__':
    parsed_stacks1 = parse_stacks(stacks)
    parsed_stacks2 = parse_stacks(stacks)
    parsed_moves = parse_moves(moves)
    for stack_move in parsed_moves:
        move(parsed_stacks1, stack_move)
        move_multiple(parsed_stacks2, stack_move)
    tops1 = ''.join([row[0] for row in parsed_stacks1])
    tops2 = ''.join([row[0] for row in parsed_stacks2])
    print(tops1, tops2)


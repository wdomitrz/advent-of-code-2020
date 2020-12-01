#!/usr/bin/env python3

with open('input.txt') as f:
    data = map(int, f.readlines())


def solve(data, S=2020):
    was = [False for i in range(S + 1)]

    for a in data:
        if a <= S and was[S-a]:
            return a * (S - a)
        was[a] = True
    return 0

print(solve(data))

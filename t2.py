#!/usr/bin/env python3

with open('input.txt') as f:
    data = map(int, f.readlines())


def solve(data, S=2020):
    was = [False for i in range(S + 1)]
    was_list = []
    was2 = [False for i in range(S + 1)]
    was2_value = [-1 for i in range(S + 1)]

    for a in data:
        if a <= S and was2[S-a]:
            return a * (S - a - was2_value[S-a]) * was2_value[S-a]

        for w in was_list:
            if a + w <= S:
                was2[a + w] = True
                was2_value[a + w] = a

        if not was[a]:
            was[a] = True
            was_list.append(a)

    return 0

print(solve(data))

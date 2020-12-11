from math import prod
import numpy as np


def count_trees(trees, initial_pos=None, slope=None):
    """
    >>> count_trees(["..##.......",\
                     "#...#...#..",\
                     ".#....#..#.",\
                     "..#.#...#.#",\
                     ".#...##..#.",\
                     "..#.##.....",\
                     ".#.#.#....#",\
                     ".#........#",\
                     "#.##...#...",\
                     "#...##....#",\
                     ".#..#...#.#"])
    7
    """
    if initial_pos is None:
        initial_pos = (0, 0)
    if slope is None:
        slope = (1, 3)

    pos = np.array(initial_pos)
    slope = np.array(slope)
    M = len(trees[0])

    res = 0
    while pos[0] < len(trees):
        if trees[pos[0]][pos[1]] == '#':
            res += 1
        pos += slope
        pos[1] %= M
    return res


def count_all_trees(trees, slopes=None):
    """
    >>> list(count_all_trees(["..##.......",\
                              "#...#...#..",\
                              ".#....#..#.",\
                              "..#.#...#.#",\
                              ".#...##..#.",\
                              "..#.##.....",\
                              ".#.#.#....#",\
                              ".#........#",\
                              "#.##...#...",\
                              "#...##....#",\
                              ".#..#...#.#"]))
    [2, 7, 3, 4, 2]
    """
    if slopes is None:
        slopes = [(1, 1), (1, 3), (1, 5), (1, 7), (2, 1)]
    return map(lambda slope: count_trees(trees, slope=slope), slopes)


def main():
    with open("inputs/d03.txt") as f:
        data = f.read().splitlines()

    print(count_trees(data))
    print(prod(count_all_trees(data)))


if __name__ == '__main__':
    import doctest
    doctest.testmod()

    main()

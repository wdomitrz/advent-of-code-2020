from math import prod

from d03_part1 import count_trees


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
    with open("d03_input.txt") as f:
        data = f.read().splitlines()

    print(prod(count_all_trees(data)))


if __name__ == '__main__':
    import doctest
    doctest.testmod()

    main()

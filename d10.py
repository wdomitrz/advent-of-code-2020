def part1(data):
    """
    >>> part1([16, 10, 15, 5, 1, 11, 7, 19, 6, 12, 4])
    35
    >>> part1([28, 33, 18, 42, 31, 14, 46, 20, 48, 47, 24, 23, 49, 45, 19, 38, 39, 11, 1, 32, 25, 35, 8, 17, 7, 9, 4, 2, 34, 10, 3])
    220
    """  # pylint: disable=line-too-long
    data = data.copy()
    data += [0, max(data) + 3]
    data = sorted(data)

    differences = [0 for _ in range(3 + 1)]
    for x, y in zip(data, data[1:]):
        differences[y - x] += 1

    return differences[1] * differences[3]


def part2(data):
    """
    >>> part2([16, 10, 15, 5, 1, 11, 7, 19, 6, 12, 4])
    8
    >>> part2([28, 33, 18, 42, 31, 14, 46, 20, 48, 47, 24, 23, 49, 45, 19, 38, 39, 11, 1, 32, 25, 35, 8, 17, 7, 9, 4, 2, 34, 10, 3])
    19208
    """  # pylint: disable=line-too-long
    combinations_up_to = {0: 1}
    for d in sorted(data):
        val = 0
        for i in range(1, 3 + 1):
            if d - i in combinations_up_to:
                val += combinations_up_to[d - i]
        combinations_up_to[d] = val
    return combinations_up_to[max(data)]


def main():
    with open("inputs/d10.txt") as f:
        data = list(map(int, f.readlines()))

    print(part1(data))
    print(part2(data))


if __name__ == '__main__':
    import doctest
    doctest.testmod()

    main()

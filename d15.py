def simulate(start, turns):
    """
    >>> [simulate([0, 3, 6], i) for i in range(1, 10+1)]
    [0, 3, 6, 0, 3, 3, 1, 0, 4, 0]
    """
    spoken = {}
    prev = -1  # Number that will never normally occur
    for i in range(turns):
        if i < len(start):
            num = start[i]
        else:
            if prev not in spoken:
                num = 0
            else:
                num = i - spoken[prev]
        spoken[prev] = i
        prev = num
    return num


def main():
    with open("inputs/d15.txt") as f:
        data = list(map(int, f.read().split(",")))

    print(simulate(data, 2020))
    print(simulate(data, 30000000))


if __name__ == '__main__':
    import doctest
    doctest.testmod()

    main()

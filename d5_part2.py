from d5_part1 import decode_number


def find_missing_id(seats):
    """
    >>> find_missing_id([1, 2, 4])
    3
    """
    seats = list(seats)
    min_id = min(seats)
    max_id = max(seats)
    M = max_id - min_id + 1
    return min_id + M * (M - 1) // 2 - sum(map(lambda x: x - min_id, seats))


def main():
    with open("d5_input.txt") as f:
        data = f.read().split()

    print(find_missing_id(map(decode_number, data)))


if __name__ == '__main__':
    import doctest
    doctest.testmod()

    main()

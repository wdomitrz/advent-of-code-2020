from d05_part1 import decode_number


def find_missing_id(seats):
    """
    >>> find_missing_id([1, 2, 4])
    3
    """
    seats = list(seats)
    max_id = max(seats)
    # Sum of all ids - sum of existing ids = value of missing id
    return (len(seats) + 1) * (2 * max_id - len(seats)) // 2 - sum(seats)


def main():
    with open("d05_input.txt") as f:
        data = f.read().split()

    print(find_missing_id(map(decode_number, data)))


if __name__ == '__main__':
    import doctest
    doctest.testmod()

    main()

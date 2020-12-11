def decode_number(s: str) -> int:
    """
    >>> decode_number("BFFFBBFRRR")
    567
    >>> decode_number("FFFBBBFRRR")
    119
    >>> decode_number("BBFFBBFRLL")
    820
    """
    return int(
        s.replace("F", "0").replace("B", "1")
        .replace("L", "0").replace("R", "1"),
        2)


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
    with open("inputs/d05.txt") as f:
        data = f.read().split()

    print(max(map(decode_number, data)))
    print(find_missing_id(map(decode_number, data)))


if __name__ == '__main__':
    import doctest
    doctest.testmod()

    main()

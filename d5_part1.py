def decode_number(s: str) -> int:
    """
    >>> decode_number("BFFFBBFRRR")
    567
    >>> decode_number("FFFBBBFRRR")
    119
    >>> decode_number("BBFFBBFRLL")
    820
    """
    s = s.replace("F", "0")
    s = s.replace("B", "1")
    s = s.replace("L", "0")
    s = s.replace("R", "1")
    return int(s, 2)


def main():
    with open("d5_input.txt") as f:
        data = f.read().split()

    print(max(map(decode_number, data)))


if __name__ == '__main__':
    import doctest
    doctest.testmod()

    main()

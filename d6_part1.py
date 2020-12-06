import string


def count_anyone_yes(group_data):
    """
    >>> count_anyone_yes("abc")
    3
    >>> count_anyone_yes("a\\nb\\nc")
    3
    >>> count_anyone_yes("ab\\nac")
    3
    >>> count_anyone_yes("a\\na\\na\\na")
    1
    >>> count_anyone_yes("b")
    1
    """
    was = [False for i in string.ascii_lowercase]

    for c in group_data:
        if c.isalpha():
            was[ord(c) - ord('a')] = True
    return sum(was)


def main():
    with open("d6_input.txt") as f:
        data = f.read().split("\n\n")

    print(sum(map(count_anyone_yes, data)))


if __name__ == '__main__':
    import doctest
    doctest.testmod()

    main()

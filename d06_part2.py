import string


def count_everyone_yes(group_data):
    """
    >>> count_everyone_yes("abc")
    3
    >>> count_everyone_yes("a\\nb\\nc")
    0
    >>> count_everyone_yes("ab\\nac")
    1
    >>> count_everyone_yes("a\\na\\na\\na")
    1
    >>> count_everyone_yes("b")
    1
    """
    was = set(string.ascii_lowercase)

    for person_ans in group_data.split():
        was &= set(person_ans)
    return len(was)


def main():
    with open("d06_input.txt") as f:
        data = f.read().split("\n\n")

    print(sum(map(count_everyone_yes, data)))


if __name__ == '__main__':
    import doctest
    doctest.testmod()

    main()

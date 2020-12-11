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
    with open("inputs/d06.txt") as f:
        data = f.read().split("\n\n")

    print(sum(map(count_anyone_yes, data)))
    print(sum(map(count_everyone_yes, data)))


if __name__ == '__main__':
    import doctest
    doctest.testmod()

    main()

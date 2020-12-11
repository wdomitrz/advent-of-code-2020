def proc_line(line):
    """
    >>> proc_line("1-3 a: abcde")
    {'min_occurences': 1, 'max_occurences': 3, 'letter': 'a', 'password': 'abcde'}
    >>> proc_line("1-3 b: cdefg")
    {'min_occurences': 1, 'max_occurences': 3, 'letter': 'b', 'password': 'cdefg'}
    >>> proc_line("2-9 c: ccccccccc")
    {'min_occurences': 2, 'max_occurences': 9, 'letter': 'c', 'password': 'ccccccccc'}
    """
    parts = line.split()
    min_occurences, max_occurences = map(int, parts[0].split('-'))
    letter = parts[1][0]
    password = parts[2]
    return {
        'min_occurences': min_occurences,
        'max_occurences': max_occurences,
        'letter': letter,
        'password': password}


def validate(min_occurences, max_occurences, letter, password):
    """
    >>> validate(min_occurences=1, max_occurences=3, letter='a', password='abcde')
    True
    >>> validate(min_occurences=1, max_occurences=3, letter='b', password='cdefg')
    False
    >>> validate(min_occurences=2, max_occurences=9, letter='c', password='ccccccccc')
    True
    """
    count = 0
    for a in password:
        if a == letter:
            count += 1
    if min_occurences <= count and count <= max_occurences:
        return True
    return False


def main():
    with open("d02_input.txt") as f:
        data = f.readlines()
    data = map(proc_line, data)
    oks = map(lambda x: validate(**x), data)
    res = sum(oks)
    print(res)


if __name__ == '__main__':
    import doctest
    doctest.testmod()

    main()

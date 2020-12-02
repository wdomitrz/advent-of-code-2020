def proc_line(line):
    """
    >>> proc_line("1-3 a: abcde")
    {'positions': [1, 3], 'letter': 'a', 'passowrd': 'abcde'}
    >>> proc_line("1-3 b: cdefg")
    {'positions': [1, 3], 'letter': 'b', 'passowrd': 'cdefg'}
    >>> proc_line("2-9 c: ccccccccc")
    {'positions': [2, 9], 'letter': 'c', 'passowrd': 'ccccccccc'}
    """
    parts = line.split()
    positions = list(map(int, parts[0].split('-')))
    letter = parts[1][0]
    password = parts[2]
    return {
        'positions': positions,
        'letter': letter,
        'passowrd': password}


def validate(positions, letter, passowrd):
    """
    >>> validate(positions=[1, 3], letter='a', passowrd='abcde')
    True
    >>> validate(positions=[1, 3], letter='b', passowrd='cdefg')
    False
    >>> validate(positions=[2, 9], letter='c', passowrd='ccccccccc')
    False
    """
    return sum(map(lambda a: a == letter, [
               passowrd[i - 1] for i in positions if i - 1 < len(passowrd)])) == 1


def main():
    with open("input.txt") as f:
        data = f.readlines()
    data = map(proc_line, data)
    oks = map(lambda x: validate(**x), data)
    res = sum(oks)
    print(res)


if __name__ == '__main__':
    import doctest
    doctest.testmod()
    
    main()

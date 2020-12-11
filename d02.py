def proc_line1(line):
    """
    >>> proc_line1("1-3 a: abcde")
    {'min_occurences': 1, 'max_occurences': 3, 'letter': 'a', 'password': 'abcde'}
    >>> proc_line1("1-3 b: cdefg")
    {'min_occurences': 1, 'max_occurences': 3, 'letter': 'b', 'password': 'cdefg'}
    >>> proc_line1("2-9 c: ccccccccc")
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


def validate1(min_occurences, max_occurences, letter, password):
    """
    >>> validate1(min_occurences=1, max_occurences=3, letter='a', password='abcde')
    True
    >>> validate1(min_occurences=1, max_occurences=3, letter='b', password='cdefg')
    False
    >>> validate1(min_occurences=2, max_occurences=9, letter='c', password='ccccccccc')
    True
    """
    count = 0
    for a in password:
        if a == letter:
            count += 1
    if min_occurences <= count and count <= max_occurences:
        return True
    return False


def proc_line2(line):
    """
    >>> proc_line2("1-3 a: abcde")
    {'positions': [1, 3], 'letter': 'a', 'passowrd': 'abcde'}
    >>> proc_line2("1-3 b: cdefg")
    {'positions': [1, 3], 'letter': 'b', 'passowrd': 'cdefg'}
    >>> proc_line2("2-9 c: ccccccccc")
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


def validate2(positions, letter, passowrd):
    """
    >>> validate2(positions=[1, 3], letter='a', passowrd='abcde')
    True
    >>> validate2(positions=[1, 3], letter='b', passowrd='cdefg')
    False
    >>> validate2(positions=[2, 9], letter='c', passowrd='ccccccccc')
    False
    """
    return sum(map(lambda a: a == letter, [
               passowrd[i - 1] for i in positions if i - 1 < len(passowrd)])) == 1


def main():
    with open("inputs/d02.txt") as f:
        data = f.readlines()

    print(sum(map(lambda x: validate1(**x), map(proc_line1, data))))
    print(sum(map(lambda x: validate2(**x), map(proc_line2, data))))


if __name__ == '__main__':
    import doctest
    doctest.testmod()

    main()

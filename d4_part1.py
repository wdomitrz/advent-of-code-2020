def parse(line):
    """
    >>> parse('ecl:gry pid:860033327 eyr:2020 hcl:#fffffd\\nbyr:1937 iyr:2017 cid:147 hgt:183cm')
    {'ecl': 'gry', 'pid': '860033327', 'eyr': '2020', 'hcl': '#fffffd', 'byr': '1937', 'iyr': '2017', 'cid': '147', 'hgt': '183cm'}
    >>> parse('iyr:2013 ecl:amb cid:350 eyr:2023 pid:028048884\\nhcl:#cfa07d byr:1929')
    {'iyr': '2013', 'ecl': 'amb', 'cid': '350', 'eyr': '2023', 'pid': '028048884', 'hcl': '#cfa07d', 'byr': '1929'}
    >>> parse('hcl:#ae17e1 iyr:2013\\neyr:2024\\necl:brn pid:760753108 byr:1931\\nhgt:179cm')
    {'hcl': '#ae17e1', 'iyr': '2013', 'eyr': '2024', 'ecl': 'brn', 'pid': '760753108', 'byr': '1931', 'hgt': '179cm'}
    >>> parse('hcl:#cfa07d eyr:2025 pid:166559648\\niyr:2011 ecl:brn hgt:59in')
    {'hcl': '#cfa07d', 'eyr': '2025', 'pid': '166559648', 'iyr': '2011', 'ecl': 'brn', 'hgt': '59in'}
    """  # pylint: disable=line-too-long

    return {name: value for field in line.split()
            for name, value in [field.split(':', 1)]}


def parse_all(data):
    """
    >>> list(parse_all('ecl:gry pid:860033327 eyr:2020 hcl:#fffffd\\nbyr:1937 iyr:2017 cid:147 hgt:183cm\\n\\niyr:2013 ecl:amb cid:350 eyr:2023 pid:028048884\\nhcl:#cfa07d byr:1929\\n\\nhcl:#ae17e1 iyr:2013\\neyr:2024\\necl:brn pid:760753108 byr:1931\\nhgt:179cm\\n\\nhcl:#cfa07d eyr:2025 pid:166559648\\niyr:2011 ecl:brn hgt:59in'))
    [{'ecl': 'gry', 'pid': '860033327', 'eyr': '2020', 'hcl': '#fffffd', 'byr': '1937', 'iyr': '2017', 'cid': '147', 'hgt': '183cm'}, {'iyr': '2013', 'ecl': 'amb', 'cid': '350', 'eyr': '2023', 'pid': '028048884', 'hcl': '#cfa07d', 'byr': '1929'}, {'hcl': '#ae17e1', 'iyr': '2013', 'eyr': '2024', 'ecl': 'brn', 'pid': '760753108', 'byr': '1931', 'hgt': '179cm'}, {'hcl': '#cfa07d', 'eyr': '2025', 'pid': '166559648', 'iyr': '2011', 'ecl': 'brn', 'hgt': '59in'}]
    """  # pylint: disable=line-too-long
    lines = data.split('\n\n')
    return map(parse, lines)


def validate(passport):
    """
    >> validate({'ecl': 'gry', 'pid': '860033327', 'eyr': '2020', 'hcl': '#fffffd', 'byr': '1937', 'iyr': '2017', 'cid': '147', 'hgt': '183cm'})
    True
    >> validate({'iyr': '2013', 'ecl': 'amb', 'cid': '350', 'eyr': '2023', 'pid': '028048884', 'hcl': '#cfa07d', 'byr': '1929'})
    False
    >> validate({'hcl': '#ae17e1', 'iyr': '2013', 'eyr': '2024', 'ecl': 'brn', 'pid': '760753108', 'byr': '1931', 'hgt': '179cm'})
    True
    >> validate({'hcl': '#cfa07d', 'eyr': '2025', 'pid': '166559648', 'iyr': '2011', 'ecl': 'brn', 'hgt': '59in'})
    False
    """  # pylint: disable=line-too-long
    mandatory_fields = ["byr", "iyr", "eyr", "hgt", "hcl",
                        "ecl", "pid", "cid"][:-1]  # We want to ignore "cid"
    return all(map(lambda k: k in passport.keys(), mandatory_fields))


def count_ok(passports, validate_fn=validate):
    """
    >>> count_ok([{'ecl': 'gry', 'pid': '860033327', 'eyr': '2020', 'hcl': '#fffffd', 'byr': '1937', 'iyr': '2017', 'cid': '147', 'hgt': '183cm'}, {'iyr': '2013', 'ecl': 'amb', 'cid': '350', 'eyr': '2023', 'pid': '028048884', 'hcl': '#cfa07d', 'byr': '1929'}, {'hcl': '#ae17e1', 'iyr': '2013', 'eyr': '2024', 'ecl': 'brn', 'pid': '760753108', 'byr': '1931', 'hgt': '179cm'}, {'hcl': '#cfa07d', 'eyr': '2025', 'pid': '166559648', 'iyr': '2011', 'ecl': 'brn', 'hgt': '59in'}])
    2
    """  # pylint: disable=line-too-long
    return sum(map(validate_fn, passports))


def main():
    with open("d4_input.txt") as f:
        data = f.read()

    print(count_ok(parse_all(data)))


if __name__ == '__main__':
    import doctest
    doctest.testmod()

    main()

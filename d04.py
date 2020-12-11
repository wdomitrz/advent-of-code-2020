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


def validate1(passport):
    """
    >> validate1({'ecl': 'gry', 'pid': '860033327', 'eyr': '2020', 'hcl': '#fffffd', 'byr': '1937', 'iyr': '2017', 'cid': '147', 'hgt': '183cm'})
    True
    >> validate1({'iyr': '2013', 'ecl': 'amb', 'cid': '350', 'eyr': '2023', 'pid': '028048884', 'hcl': '#cfa07d', 'byr': '1929'})
    False
    >> validate1({'hcl': '#ae17e1', 'iyr': '2013', 'eyr': '2024', 'ecl': 'brn', 'pid': '760753108', 'byr': '1931', 'hgt': '179cm'})
    True
    >> validate1({'hcl': '#cfa07d', 'eyr': '2025', 'pid': '166559648', 'iyr': '2011', 'ecl': 'brn', 'hgt': '59in'})
    False
    """  # pylint: disable=line-too-long
    mandatory_fields = ["byr", "iyr", "eyr", "hgt", "hcl",
                        "ecl", "pid", "cid"][:-1]  # We want to ignore "cid"
    return all(map(lambda k: k in passport.keys(), mandatory_fields))


def count_ok(passports, validate_fn=validate1):
    """
    >>> count_ok([{'ecl': 'gry', 'pid': '860033327', 'eyr': '2020', 'hcl': '#fffffd', 'byr': '1937', 'iyr': '2017', 'cid': '147', 'hgt': '183cm'}, {'iyr': '2013', 'ecl': 'amb', 'cid': '350', 'eyr': '2023', 'pid': '028048884', 'hcl': '#cfa07d', 'byr': '1929'}, {'hcl': '#ae17e1', 'iyr': '2013', 'eyr': '2024', 'ecl': 'brn', 'pid': '760753108', 'byr': '1931', 'hgt': '179cm'}, {'hcl': '#cfa07d', 'eyr': '2025', 'pid': '166559648', 'iyr': '2011', 'ecl': 'brn', 'hgt': '59in'}])
    2
    """  # pylint: disable=line-too-long
    return sum(map(validate_fn, passports))


def validate_n_digits(n: int = 4) -> bool:
    """
    >>> validate_n_digits()("")
    False
    >>> validate_n_digits()("a")
    False
    >>> validate_n_digits()("asdf")
    False
    >>> validate_n_digits()("asdfghj")
    False
    >>> validate_n_digits()("123")
    False
    >>> validate_n_digits()("1234")
    True
    >>> validate_n_digits()("1235678")
    False
    >>> validate_n_digits(n=9)("000000001")
    True
    >>> validate_n_digits(n=9)("0123456789")
    False
    """
    def func(s: str):
        if len(s) != n:
            return False
        if not s.isdigit():
            return False
        return True
    return func


def validate_n_digits_range(min_val: int, max_val: int, n: int = 4) -> bool:
    """
    >>> validate_n_digits_range(1920, 2002)("2002")
    True
    >>> validate_n_digits_range(1920, 2002)("2003")
    False
    """
    def func(s: str):
        return validate_n_digits(n)(s) and min_val <= int(s) <= max_val
    return func


valdiate_byr = validate_n_digits_range(1920, 2002)
validate_iyr = validate_n_digits_range(2010, 2020)
validate_eyr = validate_n_digits_range(2020, 2030)
validate_pid = validate_n_digits(n=9)


def validate_hgt(hgt: str) -> bool:
    """
    >>> validate_hgt("60in")
    True
    >>> validate_hgt("190cm")
    True
    >>> validate_hgt("190in")
    False
    >>> validate_hgt("190")
    False
    """
    if hgt[-2:] == 'cm':
        return 150 <= int(hgt[:-2]) <= 193
    if hgt[-2:] == 'in':
        return 59 <= int(hgt[:-2]) <= 76
    return False


def validate_hcl(hcl: str) -> bool:
    """
    >>> validate_hcl("#123abc")
    True
    >>> validate_hcl("#123abz")
    False
    >>> validate_hcl("123abc")
    False
    >>> validate_hcl("#000000")
    True
    >>> validate_hcl("#999999")
    True
    >>> validate_hcl("#aaaaaa")
    True
    >>> validate_hcl("#ffffff")
    True
    """
    if len(hcl) != 7 or hcl[0] != '#':
        return False
    for x in hcl[1:]:
        if x not in list(map(str, range(9 + 1))) + \
                list(map(chr, range(ord('a'), ord('f') + 1))):
            return False
    return True


def validate_ecl(ecl: str) -> bool:
    """
    >>> validate_ecl("brn")
    True
    >>> validate_ecl("wat")
    False
    """
    return ecl in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]


validators = {
    "byr": valdiate_byr,
    "iyr": validate_iyr,
    "eyr": validate_eyr,
    "hgt": validate_hgt,
    "hcl": validate_hcl,
    "ecl": validate_ecl,
    "pid": validate_pid}


def validate2(passport):
    """
    >>> validate2(parse("eyr:1972 cid:100\\nhcl:#18171d ecl:amb hgt:170 pid:186cm iyr:2018 byr:1926"))
    False
    >>> validate2(parse("iyr:2019\\nhcl:#602927 eyr:1967 hgt:170cm\\necl:grn pid:012533040 byr:1946"))
    False
    >>> validate2(parse("hcl:dab227 iyr:2012\\necl:brn hgt:182cm pid:021572410 eyr:2020 byr:1992 cid:277"))
    False
    >>> validate2(parse("hgt:59cm ecl:zzz\\neyr:2038 hcl:74454a iyr:2023\\npid:3556412378 byr:2007"))
    False
    >>> validate2(parse("pid:087499704 hgt:74in ecl:grn iyr:2012 eyr:2030 byr:1980\\nhcl:#623a2f"))
    True
    >>> validate2(parse("eyr:2029 ecl:blu cid:129 byr:1989\\niyr:2014 pid:896056539 hcl:#a97842 hgt:165cm"))
    True
    >>> validate2(parse("hcl:#888785\\nhgt:164cm byr:2001 iyr:2015 cid:88\\npid:545766238 ecl:hzl\\neyr:2022"))
    True
    >>> validate2(parse("iyr:2010 hgt:158cm hcl:#b6652a ecl:blu byr:1944 eyr:2021 pid:093154719"))
    True
    """  # pylint: disable=line-too-long
    mandatory_fields = ["byr", "iyr", "eyr", "hgt", "hcl",
                        "ecl", "pid", "cid"][:-1]  # We want to ignore "cid"
    return all(map(lambda k: k in passport.keys()
                   and validators[k](passport[k]), mandatory_fields))


def main():
    with open("inputs/d04.txt") as f:
        data = f.read()

    print(count_ok(parse_all(data)))
    print(count_ok(parse_all(data), validate_fn=validate2))


if __name__ == '__main__':
    import doctest
    doctest.testmod()

    main()

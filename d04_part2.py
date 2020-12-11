from d04_part1 import parse_all, count_ok


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


def validate(passport):
    """
    >>> from d04_part1 import parse
    >>> validate(parse("eyr:1972 cid:100\\nhcl:#18171d ecl:amb hgt:170 pid:186cm iyr:2018 byr:1926"))
    False
    >>> validate(parse("iyr:2019\\nhcl:#602927 eyr:1967 hgt:170cm\\necl:grn pid:012533040 byr:1946"))
    False
    >>> validate(parse("hcl:dab227 iyr:2012\\necl:brn hgt:182cm pid:021572410 eyr:2020 byr:1992 cid:277"))
    False
    >>> validate(parse("hgt:59cm ecl:zzz\\neyr:2038 hcl:74454a iyr:2023\\npid:3556412378 byr:2007"))
    False
    >>> validate(parse("pid:087499704 hgt:74in ecl:grn iyr:2012 eyr:2030 byr:1980\\nhcl:#623a2f"))
    True
    >>> validate(parse("eyr:2029 ecl:blu cid:129 byr:1989\\niyr:2014 pid:896056539 hcl:#a97842 hgt:165cm"))
    True
    >>> validate(parse("hcl:#888785\\nhgt:164cm byr:2001 iyr:2015 cid:88\\npid:545766238 ecl:hzl\\neyr:2022"))
    True
    >>> validate(parse("iyr:2010 hgt:158cm hcl:#b6652a ecl:blu byr:1944 eyr:2021 pid:093154719"))
    True
    """  # pylint: disable=line-too-long
    mandatory_fields = ["byr", "iyr", "eyr", "hgt", "hcl",
                        "ecl", "pid", "cid"][:-1]  # We want to ignore "cid"
    return all(map(lambda k: k in passport.keys()
                   and validators[k](passport[k]), mandatory_fields))


def main():
    with open("d04_input.txt") as f:
        data = f.read()

    print(count_ok(parse_all(data), validate_fn=validate))


if __name__ == '__main__':
    import doctest
    doctest.testmod()

    main()

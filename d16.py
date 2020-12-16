from math import prod


class Rules:
    def __init__(self, desc):
        ranges_values = {}
        for t in desc.splitlines():
            name, ranges = t.split(': ', 2)
            for range_begin, range_end in map(lambda x: map(
                    int, x.split("-", 2)), ranges.split(" or ")):
                ranges_values[(range_begin, range_end)] = name
        self.desc = ranges_values

    def is_valid(self, x):
        if isinstance(x, int):
            for db, de in self.desc:
                if db <= x <= de:
                    return True
            return False
        return all(map(self.is_valid, x))

    def get_possible_fields(self, x):
        res = set()
        for (db, de), v in self.desc.items():
            if db <= x <= de:
                res.add(v)
        return res

    def determine_fields(self, pos):
        res = [set.intersection(*list(map(self.get_possible_fields, l)))
               for l in pos]
        was = set()
        while len(was) != len(res):
            was = set([list(r)[0] for r in res if len(r) == 1])
            res = [r if len(r) == 1 else r - was for r in res]
        return [list(r)[0] for r in res]


def parse_my(my_desc):
    return parse_ticket(my_desc.splitlines()[1])


def parse_rest(tickets):
    return list(map(parse_ticket, tickets.splitlines()[1:]))


def parse_ticket(ticket):
    return list(map(int, ticket.split(",")))


def parse(data):
    desc, my, rest = data.split("\n\n", 3)

    return Rules(desc), parse_my(my), parse_rest(rest)


def get_departures(fields, my):
    res = []
    for field, val in zip(fields, my):
        if field.startswith("departure"):
            res.append(val)
    return res


def transpose(ls):
    return list(map(list, zip(*ls)))


def main():
    """
    >>> desc, my, tickets = parse("class: 1-3 or 5-7\\nrow: 6-11 or 33-44\\nseat: 13-40 or 45-50\\n\\nyour ticket:\\n7,1,14\\n\\nnearby tickets:\\n7,3,47\\n40,4,50\\n55,2,20\\n38,6,12")
    >>> sum(map(sum, map(lambda ticket: filter(lambda x: not desc.is_valid(x), ticket), tickets)))
    71
    >>> desc, my, tickets = parse("class: 0-1 or 4-19\\nrow: 0-5 or 8-19\\nseat: 0-13 or 16-19\\n\\nyour ticket:\\n11,12,13\\n\\nnearby tickets:\\n3,9,18\\n15,1,5\\n5,14,9")
    >>> desc.determine_fields(transpose(list(filter(desc.is_valid, tickets + [my]))))
    ['row', 'class', 'seat']
    """  # pylint: disable=line-too-long
    with open("inputs/d16.txt") as f:
        data = f.read()

    desc, my, tickets = parse(data)
    print(sum(map(sum, map(lambda ticket: filter(
        lambda x: not desc.is_valid(x), ticket), tickets))))
    print(
        prod(
            get_departures(
                desc.determine_fields(
                    transpose(
                        list(
                            filter(
                                desc.is_valid,
                                tickets +
                                [my])))),
                my)))


if __name__ == '__main__':
    import doctest
    doctest.testmod()

    main()

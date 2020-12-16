from itertools import product


def parse_mask1(mask):
    """
    >>> parse_mask1("XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X")({}, 234, 11)
    {234: 73}
    >>> parse_mask1("XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X")({}, 1, 101)
    {1: 101}
    >>> parse_mask1("XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X")({}, 0, 0)
    {0: 64}
    """

    land = int("".join(map(lambda x: '0' if x == '0' else '1', mask)), 2)
    lor = int("".join(map(lambda x: '1' if x == '1' else '0', mask)), 2)

    def fun(mem, i, val):
        mem[i] = (val & land) | lor
        return mem
    return fun


def parse_mask2(mask):
    """
    >>> parse_mask1("XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X")({}, 234, 11)
    {234: 73}
    >>> parse_mask1("XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X")({}, 1, 101)
    {1: 101}
    >>> parse_mask1("XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X")({}, 0, 0)
    {0: 64}
    """

    pos_lor = list(map(lambda x: ['0', '1'] if x == 'X' else [x], mask))
    pos_land = list(map(lambda x: ['0', '1'] if x == 'X' else '1', mask))

    def fun(mem, i, val):
        for lor, land in zip(map(lambda x: int(x, 2), map("".join, product(
                *pos_lor))), map(lambda x: int(x, 2), map("".join, product(*pos_land)))):
            mem[(i & land) | lor] = val
        return mem
    return fun


def parse_instruction(mask_parser):
    def fun(line):
        instr, val = line.split(" = ", 2)
        if instr == 'mask':
            return {'instr': 'mask', 'val': mask_parser(val)}
        else:
            return {'instr': 'mem', 'id': int(instr[4:-1]), 'val': int(val)}
    return fun


def programme(instructions):
    def mask(_, __, ___):
        pass
    mem = {}
    for instr in instructions:
        if instr['instr'] == 'mask':
            mask = instr['val']
        elif instr['instr'] == 'mem':
            mask(mem, instr['id'], instr['val'])
    return mem


def main():
    with open("inputs/d14.txt") as f:
        data = f.read().splitlines()

    print(sum(programme(map(parse_instruction(parse_mask1), data)).values()))
    print(sum(programme(map(parse_instruction(parse_mask2), data)).values()))


if __name__ == '__main__':
    import doctest
    doctest.testmod()

    main()

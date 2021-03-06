def parse_instruction(line):
    """
    >>> parse_instruction("nop +0")
    ['nop', 0]
    >>> parse_instruction("acc +1")
    ['acc', 1]
    >>> parse_instruction("jmp +4")
    ['jmp', 4]
    >>> parse_instruction("acc +3")
    ['acc', 3]
    >>> parse_instruction("jmp -3")
    ['jmp', -3]
    >>> parse_instruction("acc -99")
    ['acc', -99]
    >>> parse_instruction("acc +1")
    ['acc', 1]
    >>> parse_instruction("jmp -4")
    ['jmp', -4]
    >>> parse_instruction("acc +6")
    ['acc', 6]
    """
    instr, arg_str = line.split(' ', 1)
    arg = int(arg_str)
    return [instr, arg]


def run_till_loop(programme):
    """
    >>> run_till_loop([['nop', 0], ['acc', 1], ['jmp', 4], ['acc', 3], ['jmp', -3], ['acc', -99], ['acc', 1], ['jmp', -4], ['acc', 6]])
    (5, False)
    """  # pylint: disable=line-too-long
    was = [False for _ in programme]
    i = 0
    acc = 0

    while 0 <= i < len(was) and not was[i]:
        was[i] = True
        instr, arg = programme[i]
        if instr == 'acc':
            acc += arg
        elif instr == 'jmp':
            i += arg
            continue
        elif instr == 'nop':
            pass
        else:
            raise RuntimeError("Unknown instruction")
        i += 1

    return acc, i == len(was)


def find_bad_jmp_or_nop_value(programme):
    """
    >>> find_bad_jmp_or_nop_value([['nop', 0], ['acc', 1], ['jmp', 4], ['acc', 3], ['jmp', -3], ['acc', -99], ['acc', 1], ['jmp', -4], ['acc', 6]])
    8
    """  # pylint: disable=line-too-long
    for i, (instr, _) in enumerate(programme):
        if instr == 'jmp':
            programme[i][0] = 'nop'
        elif instr == 'nop':
            programme[i][0] = 'jmp'
        else:
            continue
        val, ok = run_till_loop(programme)
        if ok:
            return val
        programme[i][0] = instr
    return None


def main():
    with open("inputs/d08.txt") as f:
        data = f.read().splitlines()

    print(run_till_loop(list(map(parse_instruction, data)))[0])
    print(find_bad_jmp_or_nop_value(list(map(parse_instruction, data))))


if __name__ == '__main__':
    import doctest
    doctest.testmod()

    main()

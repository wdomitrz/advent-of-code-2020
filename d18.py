class Number1:
    def __init__(self, n):
        self.n = n

    def __add__(self, b):
        return Number1(self.n + b.n)

    def __sub__(self, b):
        return Number1(self.n * b.n)


class Number2:
    def __init__(self, n):
        self.n = n

    def __sub__(self, b):
        return Number2(self.n * b.n)

    def __mul__(self, b):
        return Number2(self.n + b.n)


def eval1(expr):
    """
    >>> eval1("2 * 3 + (4 * 5)")
    26
    >>> eval1("5 + (8 * 3 + 9 + 3 * 4 * 3)")
    437
    >>> eval1("5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))")
    12240
    >>> eval1("((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2")
    13632
    """
    vs = expr.replace("(", "( ").replace(")", " )").replace("*", "-")
    vs = vs.split()
    for i, v in enumerate(vs):
        if v.isdigit():
            vs[i] = "Number1(" + v + ")"
    vs = " ".join(vs)
    res = eval(vs)
    return res.n


def eval2(expr):
    """
    >>> eval2("1 + (2 * 3) + (4 * (5 + 6))")
    51
    >>> eval2("2 * 3 + (4 * 5)")
    46
    >>> eval2("5 + (8 * 3 + 9 + 3 * 4 * 3)")
    1445
    >>> eval2("5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))")
    669060
    >>> eval2("((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2")
    23340
    """
    vs = expr.replace("(", "( ").replace(")", " )").replace(
        "*", "-").replace("+", "*")
    vs = vs.split()
    for i, v in enumerate(vs):
        if v.isdigit():
            vs[i] = "Number2(" + v + ")"
    vs = " ".join(vs)
    res = eval(vs)
    return res.n


def main():
    with open("inputs/d18.txt") as f:
        data = f.read().splitlines()

    print(sum(map(eval1, data)))
    print(sum(map(eval2, data)))


if __name__ == '__main__':
    import doctest
    doctest.testmod()

    main()

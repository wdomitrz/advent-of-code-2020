from math import prod


def find_nearest(time, steps):
    """
    >>> find_nearest(939, ["7","13","x","x","59","x","31","19"])
    (5, 59)
    """
    return min(map(lambda s: (0 if (d := time % s) == 0 else s - d,
                              s), map(int, filter(lambda a: a.isdigit(), steps))))


def extended_gcd(a, b):
    """
    Returns numbers x, y, such that a * x + b * y = gcd(a, b).
    """
    old_r, r = a, b
    old_s, s = 1, 0
    old_t, t = 0, 1
    while r != 0:
        quotioent = old_r // r
        old_r, r = r, old_r - quotioent * r
        old_s, s = s, old_s - quotioent * s
        old_t, t = t, old_t - quotioent * t
    x, y = old_s, old_t
    return x, y


def find_earliest(vals):
    """
    >>> find_earliest(["7","13","x","x","59","x","31","19"])
    1068781
    >>> find_earliest(["17","x","13","19"])
    3417
    >>> find_earliest(["67","7","59","61"])
    754018
    >>> find_earliest(["67","x","7","59","61"])
    779210
    >>> find_earliest(["67","7","x","59","61"])
    1261476
    >>> find_earliest(["1789","37","47","1889"])
    1202161486
    """
    vals = list(map(lambda x: 1 if x == "x" else int(x), vals))
    m = prod(vals)
    res = 0
    for i, x in enumerate(vals):
        if x == 1:
            continue
        mi = m // x
        res -= i * extended_gcd(x, mi)[1] * mi
        res %= m
    return res


def main():
    with open("inputs/d13.txt") as f:
        data = f.read().splitlines()
    data = int(data[0]), data[1].split(",")

    print(prod(find_nearest(data[0], data[1])))
    print(find_earliest(data[1]))


if __name__ == '__main__':
    import doctest
    doctest.testmod()

    main()

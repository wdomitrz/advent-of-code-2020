def product_of_n_with_fixed_sum(data, n=3, S=2020):
    """
    >>> product_of_n_with_fixed_sum([1721, 979, 366, 299, 675, 1456], n=2)
    514579
    >>> product_of_n_with_fixed_sum([1721, 979, 366, 299, 675, 1456], n=3)
    241861950
    """

    reached_by = [{} for _ in range(S + 1)]
    reached_by[0][0] = 1

    for a in data:
        for i in range(n, 0, -1):
            for x in reached_by[i - 1].keys():
                if x + a <= S:
                    reached_by[i][x + a] = a

    result = 1
    for i in range(n, 0, -1):
        a = reached_by[i][S]
        result *= a
        S -= a

    return result


def main():
    with open("input.txt") as f:
        data = f.readlines()
    data = map(int, data)
    print(product_of_n_with_fixed_sum(data, n=3))


if __name__ == '__main__':
    import doctest
    doctest.testmod()

    main()

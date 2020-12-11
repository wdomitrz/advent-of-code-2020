def product_of_two_with_fixed_sum(data, S=2020):
    """
    >>> product_of_two_with_fixed_sum([1721, 979, 366, 299, 675, 1456])
    514579
    """
    was = [False for i in range(S + 1)]

    for a in data:
        if a <= S and was[S - a]:
            return a * (S - a)
        was[a] = True


def main():
    with open("d01_input.txt") as f:
        data = f.readlines()
    data = map(int, data)
    print(product_of_two_with_fixed_sum(data))


if __name__ == '__main__':
    import doctest
    doctest.testmod()

    main()

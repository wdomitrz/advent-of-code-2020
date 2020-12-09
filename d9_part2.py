from d9_part1 import find_first_not_ok


def find_range_with_sum(s, data):
    """
    >>> find_range_with_sum(127, [35, 20, 15, 25, 47, 40, 62, 55, 65, 95, 102, 117, 150, 182, 127, 219, 299, 277, 309, 576])
    [15, 25, 47, 40]
    """  # pylint: disable=line-too-long
    i, j = 0, 2
    current_sum = data[0] + data[1]
    while j < len(data):
        if current_sum == s:
            if i + 1 == j:
                return None
            return data[i:j]

        if current_sum < s:
            current_sum += data[j]
            j += 1
        else:
            current_sum -= data[i]
            i += 1
    return None


def main():
    with open("d9_input.txt") as f:
        data = list(map(int, f.readlines()))

    res_range = find_range_with_sum(find_first_not_ok(data), data)
    print(min(res_range) + max(res_range))


if __name__ == '__main__':
    import doctest
    doctest.testmod()

    main()

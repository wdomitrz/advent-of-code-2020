def add_to_dict_added_x(x, ds, can_be_next):
    """
    >>> add_to_dict_added_x(2, [3, 4], {6: 3})
    {6: 4, 5: 1}
    """
    for d in ds:
        if x + d not in can_be_next:
            can_be_next[x + d] = 0
        can_be_next[x + d] += 1
    return can_be_next


def remove_from_dict_added_x(x, ds, can_be_next):
    """
    >>> remove_from_dict_added_x(2, [3, 4], {5: 1, 6: 3})
    {6: 2}
    """
    for d in ds:
        can_be_next[x + d] -= 1
        if can_be_next[x + d] <= 0:
            del can_be_next[x + d]
    return can_be_next


def find_first_not_ok(data, window_length=25):
    """
    >>> find_first_not_ok([35, 20, 15, 25, 47, 40, 62, 55, 65, 95, 102, 117, 150, 182, 127, 219, 299, 277, 309, 576], window_length=5)
    127
    """  # pylint: disable=line-too-long
    can_be_next = {}
    for i, d in enumerate(data):
        if i >= window_length and d not in can_be_next:
            return d

        can_be_next = add_to_dict_added_x(
            d, data[max(0, i - window_length + 1): i], can_be_next)

        if i - window_length >= 0:
            can_be_next = remove_from_dict_added_x(
                data[i - window_length], data[i - window_length + 1: i], can_be_next)

    return None


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


def sum_min_and_max(xs):
    return min(xs) + max(xs)


def main():
    with open("inputs/d09.txt") as f:
        data = list(map(int, f.readlines()))

    print(find_first_not_ok(data))
    print(sum_min_and_max(find_range_with_sum(find_first_not_ok(data), data)))


if __name__ == '__main__':
    import doctest
    doctest.testmod()

    main()

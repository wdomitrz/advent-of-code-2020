from math import prod

from d7_part1 import dfs, parse_line


def count_bags_in(bag, bag_graph):
    """
    >>> data = "shiny gold bags contain 2 dark red bags.\\ndark red bags contain 2 dark orange bags.\\ndark orange bags contain 2 dark yellow bags.\\ndark yellow bags contain 2 dark green bags.\\ndark green bags contain 2 dark blue bags.\\ndark blue bags contain 2 dark violet bags.\\ndark violet bags contain no other bags.".splitlines()
    >>> bag_graph = dict(map(parse_line, data))
    >>> count_bags_in(("shiny", "gold"), bag_graph)
    126
    """  # pylint: disable=line-too-long
    return dfs(bag, {}, bag_graph, lambda xs: 1 + sum(map(prod, xs))) - \
        1  # We don't count the outer bag.


def main():
    with open("d7_input.txt") as f:
        data = f.read().splitlines()

    bag_graph = dict(map(parse_line, data))
    print(count_bags_in(("shiny", "gold"), bag_graph))


if __name__ == '__main__':
    import doctest
    doctest.testmod()

    main()

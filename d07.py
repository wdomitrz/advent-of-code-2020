from math import prod


def parse_line(line):
    """
    >>> parse_line("light red bags contain 1 bright white bag, 2 muted yellow bags.")
    (('light', 'red'), {('bright', 'white'): 1, ('muted', 'yellow'): 2})
    >>> parse_line("dark orange bags contain 3 bright white bags, 4 muted yellow bags.")
    (('dark', 'orange'), {('bright', 'white'): 3, ('muted', 'yellow'): 4})
    >>> parse_line("bright white bags contain 1 shiny gold bag.")
    (('bright', 'white'), {('shiny', 'gold'): 1})
    >>> parse_line("muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.")
    (('muted', 'yellow'), {('shiny', 'gold'): 2, ('faded', 'blue'): 9})
    >>> parse_line("shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.")
    (('shiny', 'gold'), {('dark', 'olive'): 1, ('vibrant', 'plum'): 2})
    >>> parse_line("dark olive bags contain 3 faded blue bags, 4 dotted black bags.")
    (('dark', 'olive'), {('faded', 'blue'): 3, ('dotted', 'black'): 4})
    >>> parse_line("vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.")
    (('vibrant', 'plum'), {('faded', 'blue'): 5, ('dotted', 'black'): 6})
    >>> parse_line("faded blue bags contain no other bags.")
    (('faded', 'blue'), {})
    >>> parse_line("dotted black bags contain no other bags.")
    (('dotted', 'black'), {})
    """
    outer_bag_desc, rest = line.split("contain", 1)
    outer_bag = tuple(outer_bag_desc.split()[:2])

    if rest == " no other bags.":
        return outer_bag, {}

    inner_bags = {}
    for count, adj, color, _ in map(lambda b: b.split(), rest[:-1].split(",")):
        inner_bags[(adj, color)] = int(count)

    return outer_bag, inner_bags


def dfs(v, vis, graph, process_neighbours):
    """
    >>> dfs(1, {}, {1: {2: 1, 3: 1}, 2: {3: 2}, 3: {2: 1}, 4: {1: 2, 3: 6}}, list)
    [(1, [(2, [(1, None)])]), (1, [(1, None)])]
    """
    if v in vis:
        return vis[v]

    vis[v] = None
    neighbours_vals = map(
        lambda u_count: (
            u_count[1], dfs(
                u_count[0], vis, graph, process_neighbours)), graph[v].items())

    vis[v] = process_neighbours(neighbours_vals)
    return vis[v]


def vertice_reachability(v_end, graph):
    """
    >>> vertice_reachability(("shiny", "gold"), {('light', 'red'): {('bright', 'white'): 1, ('muted', 'yellow'): 2}, ('dark', 'orange'): {('bright', 'white'): 3, ('muted', 'yellow'): 4}, ('bright', 'white'): {('shiny', 'gold'): 1}, ('muted', 'yellow'): {('shiny', 'gold'): 2, ('faded', 'blue'): 9}, ('shiny', 'gold'): {('dark', 'olive'): 1, ('vibrant', 'plum'): 2}, ('dark', 'olive'): {('faded', 'blue'): 3, ('dotted', 'black'): 4}, ('vibrant', 'plum'): {('faded', 'blue'): 5, ('dotted', 'black'): 6}, ('faded', 'blue'): {}, ('dotted', 'black'): {}})
    {('shiny', 'gold'): True, ('light', 'red'): True, ('bright', 'white'): True, ('dark', 'orange'): True, ('muted', 'yellow'): True, ('dark', 'olive'): False, ('faded', 'blue'): False, ('dotted', 'black'): False, ('vibrant', 'plum'): False}
    """  # pylint: disable=line-too-long
    vis = {v_end: True}
    for v in graph.keys():
        dfs(v, vis, graph, process_neighbours=lambda xs: any(
            map(lambda x: x[1], xs)))
    return vis


def count_reachability(v_end, graph):
    """
    >>> count_reachability(("shiny", "gold"), {('light', 'red'): {('bright', 'white'): 1, ('muted', 'yellow'): 2}, ('dark', 'orange'): {('bright', 'white'): 3, ('muted', 'yellow'): 4}, ('bright', 'white'): {('shiny', 'gold'): 1}, ('muted', 'yellow'): {('shiny', 'gold'): 2, ('faded', 'blue'): 9}, ('shiny', 'gold'): {('dark', 'olive'): 1, ('vibrant', 'plum'): 2}, ('dark', 'olive'): {('faded', 'blue'): 3, ('dotted', 'black'): 4}, ('vibrant', 'plum'): {('faded', 'blue'): 5, ('dotted', 'black'): 6}, ('faded', 'blue'): {}, ('dotted', 'black'): {}})
    4
    """  # pylint: disable=line-too-long
    vis = vertice_reachability(v_end, graph)
    # We cannot reach vertice from itself (so we have -1)
    return sum(map(lambda x: x > 0, vis.values())) - 1


def count_bags_in(bag, bag_graph):
    """
    >>> data = "shiny gold bags contain 2 dark red bags.\\ndark red bags contain 2 dark orange bags.\\ndark orange bags contain 2 dark yellow bags.\\ndark yellow bags contain 2 dark green bags.\\ndark green bags contain 2 dark blue bags.\\ndark blue bags contain 2 dark violet bags.\\ndark violet bags contain no other bags.".splitlines()
    >>> bag_graph = dict(map(parse_line, data))
    >>> count_bags_in(("shiny", "gold"), bag_graph)
    126
    """  # pylint: disable=line-too-long
    # We don't count the outer bag (so we have -1)
    return dfs(bag, {}, bag_graph, lambda xs: 1 + sum(map(prod, xs))) - 1


def main():
    with open("inputs/d07.txt") as f:
        data = f.read().splitlines()

    bag_graph = dict(map(parse_line, data))
    print(count_reachability(("shiny", "gold"), bag_graph))
    print(count_bags_in(("shiny", "gold"), bag_graph))


if __name__ == '__main__':
    import doctest
    doctest.testmod()

    main()

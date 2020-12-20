class Grammar:

    @staticmethod
    def parse_rule(rule):
        if rule[0] == '\"':
            return [rule[1]]
        return list(map(int, rule.split(" ")))

    @staticmethod
    def parse_line(line):
        n_str, rest = line.split(": ")

        return int(n_str), list(
            map(lambda rule: Grammar.parse_rule(rule), rest.split(" | ")))

    def __init__(self, desc):
        self.rules = dict(map(self.parse_line, desc))

    def is_ok_with(self, w, rls):
        if len(rls) == 0 or len(w) == 0:
            return len(w) == len(rls) == 0

        rl = rls[0]
        rls = rls[1:]
        if isinstance(rl, str):
            return w[0] == rl and self.is_ok_with(w[1:], rls)

        return any(map(lambda rs: self.is_ok_with(
            w, rs + rls), self.rules[rl]))

    def is_ok(self, w):
        return self.is_ok_with(w, [0])

    def replace_rules(self):
        self.rules[8] = [[42], [42, 8]]
        self.rules[11] = [[42, 31], [42, 11, 31]]
        return self


def main():
    with open("inputs/d19.txt") as f:
        data = f.read().split("\n\n")
    grammar, lines = Grammar(data[0].splitlines()), data[1].splitlines()

    print(sum(map(grammar.is_ok, lines)))
    print(sum(map(grammar.replace_rules().is_ok, lines)))


if __name__ == '__main__':
    import doctest
    doctest.testmod()

    main()

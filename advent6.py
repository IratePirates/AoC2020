import itertools

def parse_input(in_f):
    f = open(in_f, 'r')
    tokens = []
    for x in f:
        if x[0] is not "\n":
            tokens += [set(x.strip())]
        else:
            yield tokens
            tokens = []
    f.close()


def part1(in_f):
    running_total = 0
    for group in parse_input(in_f):
        flattened = itertools.chain.from_iterable(group)
        running_total += len(set(flattened))
    return running_total


def check_intersection(groups, letter):
    res = [ letter in g for g in groups ]
    return all(res)


def part2(in_f):
    running_total = 0
    for group in parse_input(in_f):
        all_options = set(itertools.chain.from_iterable(group))
        for option in all_options:
            if check_intersection(group, option):
                running_total += 1
    return running_total


print(part1("test6.txt"))
print(part1("input6.txt"))
print(part2("test6.txt"))
print(part2("input6.txt"))


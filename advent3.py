import numpy


def parse_input(in_f):
    f = open(in_f, 'r')
    for x in f:
        yield x.strip()
    f.close()


def part1(in_f, x, y):
    col = 0
    cnt = 0 
    for idx, r in enumerate(parse_input(in_f)):
        if idx % y != 0:
            continue
        if r[col] == '#':
           cnt += 1
        col = (col + x) % len(r)
    return cnt


def part2(in_f):
    sleds = [(1,1),
             (3,1),
             (5,1),
             (7,1),
             (1,2)]
    
    res = [part1(in_f, s[0], s[1]) for s in sleds]
    print(res)
    print(numpy.prod(res))


print(part1("test3.txt", 3, 1))
print(part1("input3.txt", 3, 1))
part2("test3.txt")
part2("input3.txt")

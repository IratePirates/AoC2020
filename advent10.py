def parse_input(in_f):
    instr = []
    f = open(in_f, 'r')
    for x in f:
        instr.append(int(x))
    return instr


def find_diffs(in_f):
    instr = parse_input(in_f)
    instr.sort()

    diffs = [0,0,0,0]
    diff = instr[0]
    diffs [diff] += 1

    for idx, i in enumerate(instr):
        if (idx + 1) >= len(instr):
            diffs[3] += 1
            return diffs 
        diff = instr[idx + 1] - i
        diffs [diff] += 1


def part1(in_f):
    diffs = find_diffs(in_f)
    return diffs[1] * diffs[3]


assert(part1("test10.txt") == 35)
assert(part1("test10a.txt") == 220)
assert(part1("input10.txt") == 2812)


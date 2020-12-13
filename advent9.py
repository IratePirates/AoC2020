def parse_input(in_f):
    instr = []
    f = open(in_f, 'r')
    for x in f:
        instr.append(int(x))
    return instr


def check_valid(num, ra, l):
    for idx, n in enumerate(ra):
        if (num - n) in ra:
            idx2 = ra.index(num-n)
            if idx2 != idx:
                return True
    return False


def part1(in_f, l):
    instr = parse_input(in_f)
    for idx, num in enumerate(instr):
        if idx < l:
            continue
        if not check_valid(num, instr[idx-l:idx], l):
            return num


def part2(in_f, l):
    instr = parse_input(in_f)
    target = part1(in_f, l)
    
    for idx, i in enumerate(instr):
        run = []
        cnt = 0

        run.append(i)
        while sum(run) <= target:
            run.append(instr[idx+cnt+1])
            if sum(run) == target:
                run.sort()
                print(run, sum(run))
                return run[0] + run[-1] 
            cnt += 1
    return None

assert(part1("test9.txt", 5) == 127)
assert(part1("input9.txt", 25) == 15353384)
assert(part2("test9.txt", 5) == 62)
print(part2("input9.txt", 25))


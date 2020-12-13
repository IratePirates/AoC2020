import copy

def parse_input(in_f):
    instr = []
    f = open(in_f, 'r')
    for idx, x in enumerate(f):
        s = x.split(" ")
        if len(s) == 2:
            instr.append((idx, s[0].strip(), int(s[1].strip())))
    return instr


class intcode_again:
    _dispatch = {}

    def __init__(self, prog):
        self.acc = 0
        self.pc = 0
        self.prog = copy.deepcopy(prog)
        self.prog_len = len(self.prog)
        self. history =  []
        self._dispatch = { 'jmp' : lambda x : self.jump(x),
                           'acc' : lambda x : self.accumulate(x),
                           'nop' : lambda x : self.noop(x),
                         }

    def noop(self, val):
        self.pc += 1

    def jump(self, val):
        self.pc += val

    def accumulate(self, val):
        self.pc += 1
        self.acc += val 

    def run_instruction(self):
        if self.pc >= self.prog_len:
            return (self.acc, False)
        else:
            instr = self.prog[self.pc]
            if instr[0] in self.history:
                return (self.acc, True)
            else:
                self._dispatch[instr[1]](instr[2])
                self.history.append(instr[0])
                return (None, False)

    def print_state(self):
        print(f"PC: {self.pc} ACC: {self.acc}, {self.history}")

    def run(self):
        print("Starting the new intcode")
        res, looping = self.run_instruction()
        cnt = 0
        while res is None:
            res, looping = self.run_instruction()
            # self.print_state()
            cnt += 1
        return res, looping
 

def part1(in_f):
    instr = parse_input(in_f)
    interp = intcode_again(instr)
    res, looping = interp.run()
    return res


def part2(in_f):
    instr = parse_input(in_f)
    print("Initial Instr:", instr)

    for f in range(len(instr)):
        new_instr = copy.deepcopy(instr)
        if new_instr[f][1] == "nop":
            new_instr[f] = (new_instr[f][0], "jmp", new_instr[f][2])
        elif new_instr[f][1] == "jmp":
            new_instr[f] = (new_instr[f][0], "nop", new_instr[f][2])
        else:
            continue

        interp = intcode_again(new_instr)
        res, looping = interp.run()

        if looping == False:
            return(res)
    return None

#print(parse_input("input8.txt"))
#print(part1("test8.txt"))
assert(part1("test8.txt") == 5)
print(part1("input8.txt"))
assert(part1("input8.txt") == 1749)

assert(part2("test8.txt") == 8)
print(part2("input8.txt"))


